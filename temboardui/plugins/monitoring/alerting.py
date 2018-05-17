import operator


def bootstrap_checks(hostinfo):
    # Default checks with thresholds to run against monitoring data

    # Loadaverage (value)
    # Global to host
    yield ("load1", hostinfo['n_cpu'] / float(2), hostinfo['n_cpu'])
    # CPU (percent)
    # One per CPU
    yield ("cpu_core", 50, 80)
    # Memory usage (percent)
    # global
    yield ("memory", 50, 80)
    # Swap usage (percent)
    # Global to host
    yield ("swap_usage", 30, 50)
    # Filesystems usage (percent)
    # One per filesystem
    yield ("fs_usage_mountpoint", 80, 90)
    # Number of WAL files ready to be archived (value)
    # Global to postgres instance
    yield ("wal_files_archive", 10, 20)
    # Number of WAL files (value)
    # Global to postgres instance
    yield ("wal_files_total", 50, 100)
    # Number of transaction rollback (value)
    # One per DB
    yield ("rollback_db", 10, 20)
    # Cache hitratio (percent)
    # One per DB
    yield ("hitreadratio_db", 90, 80)
    # Client sessions vs max_connections (percent)
    # Global to postgres instance
    yield ("sessions_usage", 80, 90)
    # Waiting sessions (value)
    # One per DB
    yield ("waiting_session_db", 5, 10)


class PreProcess(object):

    @staticmethod
    def loadaverage(data):
        return float(data['loadavg'][0]['load1'])

    @staticmethod
    def cpu(data):
        _data = dict()
        for r in data['cpu']:
            total = 0
            idle = 0
            total += int(r['time_system'])
            total += int(r['time_steal'])
            total += int(r['time_iowait'])
            total += int(r['time_user'])
            total += int(r['time_idle'])
            idle = int(r['time_idle'])
            _data[r['cpu']] = int((total - idle) / float(total) * 100)
        return _data

    @staticmethod
    def memory(data):
        return int(
            (int(data['memory'][0]['mem_total'])
             - int(data['memory'][0]['mem_free'])
             - int(data['memory'][0]['mem_cached']))
            / float(data['memory'][0]['mem_total']) * 100
        )

    @staticmethod
    def swap(data):
        return int(
            int(data['memory'][0]['swap_used'])
            / float(data['memory'][0]['swap_total']) * 100
        )

    @staticmethod
    def fs(data):
        _data = dict()
        for r in data['filesystems_size']:
            _data[r['mount_point']] = int(int(r['used']) / float(r['total'])
                                          * 100)
        return _data

    @staticmethod
    def archive_ready(data):
        return int(data['wal_files'][0]['archive_ready'])

    @staticmethod
    def wal_files(data):
        return int(data['wal_files'][0]['total'])

    @staticmethod
    def xacts_rollback(data):
        _data = dict()
        for r in data['xacts']:
            _data[r['dbname']] = int(r['n_rollback'])
        return _data

    @staticmethod
    def hitratio(data):
        _data = dict()
        for r in data['blocks']:
            _data[r['dbname']] = int(r['hitmiss_ratio']) \
                if int(r['blks_read']) + int(r['blks_hit']) > 0 else 100
        return _data

    @staticmethod
    def sessions(data):
        n = 0
        for r in data['sessions']:
            n += int(r['idle_in_xact'])
            n += int(r['idle_in_xact_aborted'])
            n += int(r['no_priv'])
            n += int(r['idle'])
            n += int(r['disabled'])
            n += int(r['waiting'])
            n += int(r['active'])
            n += int(r['fastpath'])
        return int(n / float(data['max_connections']) * 100)

    @staticmethod
    def waiting(data):
        _data = dict()
        for r in data['sessions']:
            _data[r['dbname']] = int(r['waiting'])
        return _data


check_specs = dict(
    load1=dict(
        type='system',
        description='Loadaverage',
        preprocess=PreProcess.loadaverage,
        message='{value} is greater than {threshold}',
        operator=operator.gt,
    ),
    cpu_core=dict(
        type='system',
        description='CPU usage',
        preprocess=PreProcess.cpu,
        message='{value}% is greater than {threshold}%',
        operator=operator.gt,
    ),
    memory=dict(
        type='system',
        description='Memory usage',
        preprocess=PreProcess.memory,
        message='{value}% is greater than {threshold}%',
        operator=operator.gt,
    ),
    swap_usage=dict(
        type='system',
        description='Swap usage',
        preprocess=PreProcess.swap,
        message='{value}% is greater than {threshold}%',
        operator=operator.gt,
    ),
    fs_usage_mountpoint=dict(
        type='system',
        description='File systems usage',
        preprocess=PreProcess.fs,
        message='{key}: {value}% is greater than {threshold}%',
        operator=operator.gt,
    ),
    wal_files_archive=dict(
        type='postgres',
        description='WAL files ready to be archived',
        preprocess=PreProcess.archive_ready,
        message='{value} is greater than {threshold}',
        operator=operator.gt,
    ),
    wal_files_total=dict(
        type='postgres',
        description='WAL files',
        preprocess=PreProcess.wal_files,
        message='{value} is greater than {threshold}',
        operator=operator.gt,
    ),
    rollback_db=dict(
        type='postgres',
        description='Rollbacked transactions',
        preprocess=PreProcess.xacts_rollback,
        message='{key}: {value} is greater than {threshold}',
        operator=operator.gt,
    ),
    hitreadratio_db=dict(
        type='postgres',
        description='Cache Hit Ratio',
        preprocess=PreProcess.hitratio,
        message='{key}: {value} is less than {threshold}',
        operator=operator.lt,
    ),
    sessions_usage=dict(
        type='postgres',
        description='Client sessions',
        preprocess=PreProcess.sessions,
        message='{value} is greater than {threshold}',
        operator=operator.gt,
    ),
    waiting_session_db=dict(
        type='postgres',
        description='Waiting sessions',
        preprocess=PreProcess.waiting,
        message='{key}: {value} is greater than {threshold}',
        operator=operator.gt,
    ),
)


def get_highest_state(states):
    """
    Returns the highest state.
    """
    levels = ['UNDEF', 'OK', 'WARNING', 'CRITICAL']
    return levels[max([levels.index(state) for state in states])]


def checks_info(session, host_id, instance_id):
    """
    Returns alerting checks with current state by host_id/instance_id
    """
    query = """
SELECT c.name, c.warning, c.critical, c.description, c.enabled,
json_agg(cs.state) AS keys_states
FROM monitoring.checks c JOIN monitoring.check_states cs ON (c.check_id = cs.check_id)
WHERE host_id = :host_id AND instance_id = :instance_id
GROUP BY 1,2,3,4,5 ORDER BY 1
    """  # noqa
    res = session.execute(query,
                          dict(host_id=host_id, instance_id=instance_id))
    ret = []
    for row in res.fetchall():
        c_row = dict(row)
        c_row['state'] = get_highest_state(c_row['keys_states'])
        del c_row['keys_states']
        ret.append(c_row)
    return ret


def check_state_detail(session, host_id, instance_id, check_name):
    query = """
SELECT json_agg(json_build_object('key', cs.key, 'state', cs.state, 'datetime',
                                  sc.datetime, 'value', sc.value, 'warning',
                                  sc.warning, 'critical', sc.critical)) AS state_detail
FROM monitoring.checks c JOIN monitoring.check_states cs ON (c.check_id = cs.check_id)
JOIN monitoring.state_changes sc ON (sc.check_id = c.check_id AND sc.key = cs.key
                                     AND sc.datetime = (SELECT MAX(datetime)
                                                        FROM monitoring.state_changes sc2
                                                        WHERE sc2.check_id=c.check_id
                                                        AND sc2.key = cs.key
                                                        AND sc2.state = cs.state))
WHERE host_id = :host_id AND instance_id = :instance_id AND c.name = :check_name
    """  # noqa
    res = session.execute(query,
                          dict(host_id=host_id, instance_id=instance_id,
                               check_name=check_name))
    row = res.fetchone()
    c_row = dict(row)
    return c_row['state_detail']
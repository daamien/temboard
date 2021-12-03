# API of the agent

## Core API {#core_api}

> User login
>
> reqheader Content-Type
>
> :   `application/json`
>
> status 200
>
> :   no error
>
> status 404
>
> :   invalid username or password
>
> status 500
>
> :   internal error
>
> status 406
>
> :   username or password malformed or missing

**Example request**:

``` http
POST /login HTTP/1.1
Content-Type: application/json

{
    "username": "alice",
    "password": "foo!!"
}
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/0.0.1 Python/2.7.8
Date: Wed, 22 Apr 2015 12:19:48 GMT
Content-type: application/json

{"session": "fa452548403ac53f2158a65f5eb6db9723d2b07238dd83f5b6d9ca52ce817b63"}
```

**Error responses**:

``` http
HTTP/1.0 404 Not Found
Server: temboard-agent/0.0.1 Python/2.7.8
Date: Wed, 22 Apr 2015 12:20:33 GMT
Content-type: application/json

{"error": "Invalid username/password."}
```

``` http
HTTP/1.0 406 Not Acceptable
Server: temboard-agent/0.0.1 Python/2.7.8
Date: Wed, 22 Apr 2015 12:21:01 GMT
Content-type: application/json

{"error": "Parameter 'password' is malformed."}
```

> User logout
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session ID
>
> status 500
>
> :   internal error
>
> status 406
>
> :   session ID malformed

**Example request**:

``` http
GET /logout HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/0.0.1 Python/2.7.8
Date: Wed, 22 Apr 2015 12:33:19 GMT
Content-type: application/json

{"logout": true}
```

**Error responses**:

``` http
HTTP/1.0 401 Unauthorized
Server: temboard-agent/0.0.1 Python/2.7.8
Date: Wed, 22 Apr 2015 12:36:33 GMT
Content-type: application/json

{"error": "Invalid session."}
```

``` http
HTTP/1.0 406 Not Acceptable
Server: temboard-agent/0.0.1 Python/2.7.8
Date: Wed, 22 Apr 2015 12:37:23 GMT
Content-type: application/json

{"error": "Parameter 'X-Session' is malformed."}
```

> Get global informations about the environment
>
> status 200
>
> :   no error
>
> status 500
>
> :   internal error

**Example request**:

``` http
GET /discover HTTP/1.1
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/0.0.1 Python/2.7.8
Date: Wed, 22 Apr 2015 12:33:19 GMT
Content-type: application/json

{
    "hostname": "neptune",
    "pg_data": "/var/lib/postgresql/9.4/main",
    "pg_port": 5432,
    "plugins": ["monitoring", "dashboard", "pgconf", "administration", "activity", "maintenance"],
    "memory_size": 8241508352,
    "pg_version": "PostgreSQL 9.4.5 on x86_64-unknown-linux-gnu, compiled by gcc (Ubuntu 4.9.2-10ubuntu13) 4.9.2, 64-bit",
    "cpu": 4
}
```

> Get current username
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session ID
>
> status 500
>
> :   internal error
>
> status 406
>
> :   session ID malformed

**Example request**:

``` http
GET /profile HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/0.0.1 Python/2.7.8
Date: Wed, 22 Apr 2015 12:33:19 GMT
Content-type: application/json

{
    "username": "alice"
}
```

**Error responses**:

``` http
HTTP/1.0 401 Unauthorized
Server: temboard-agent/0.0.1 Python/2.7.8
Date: Wed, 22 Apr 2015 12:36:33 GMT
Content-type: application/json

{"error": "Invalid session."}
```

``` http
HTTP/1.0 406 Not Acceptable
Server: temboard-agent/0.0.1 Python/2.7.8
Date: Wed, 22 Apr 2015 12:37:23 GMT
Content-type: application/json

{"error": "Parameter 'X-Session' is malformed."}
```

> Get all notifications from the agent.
>
> query key
>
> :   Agent\'s key for authentication (optional)
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session ID
>
> status 500
>
> :   internal error
>
> status 406
>
> :   session ID malformed

**Example request**:

``` http
GET /notifications HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/0.0.1 Python/2.7.8
Date: Wed, 22 Apr 2015 12:33:19 GMT
Content-type: application/json

[
    {"date": "2016-04-11T16:12:38", "username": "alice", "message": "Login"},
    {"date": "2016-04-11T16:02:03", "username": "alice", "message": "Login"},
    {"date": "2016-04-11T15:50:57", "username": "alice", "message": "PostgreSQL reload"},
    {"date": "2016-04-11T15:48:50", "username": "alice", "message": "PostgreSQL reload"}
]
```

**Error responses**:

``` http
HTTP/1.0 401 Unauthorized
Server: temboard-agent/0.0.1 Python/2.7.8
Date: Wed, 22 Apr 2015 12:36:33 GMT
Content-type: application/json

{"error": "Invalid session."}
```

``` http
HTTP/1.0 406 Not Acceptable
Server: temboard-agent/0.0.1 Python/2.7.8
Date: Wed, 22 Apr 2015 12:37:23 GMT
Content-type: application/json

{"error": "Parameter 'X-Session' is malformed."}
```

> Get informations about the agent
>
> status 200
>
> :   no error
>
> status 500
>
> :   internal error

**Example request**:

``` http
GET /status HTTP/1.1
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/2.0+master Python/2.7.5
Date: Fri, 15 Jun 2018 13:42:57 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

{
    "start_datetime": "2018-06-15T15:42:42",
    "version": "2.0+master",
    "user": "postgres",
    "reload_datetime": "2018-06-15T15:42:42",
    "pid": 32669,
    "configfile": "/etc/temboard-agent/temboard-agent.conf"
}
```

## Administration plugin API {#administration_api}

> Control PostgreSQL server. Supported actions are `start`, `stop`,
> `restart` and `reload`.
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header or parameter is malformed.

**Example request**:

``` http
POST /administration/control HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
Content-Type: application/json

{
    "action": "restart"
}
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/0.0.1 Python/2.7.8
Date: Wed, 22 Apr 2015 09:57:52 GMT
Content-type: application/json

{
    "action": "restart",
    "state": "ok"
}
```

**Error responses**:

``` http
HTTP/1.0 401 Unauthorized
Server: temboard-agent/0.0.1 Python/2.7.8
Date: Wed, 22 Apr 2015 09:58:00 GMT
Content-type: application/json

{"error": "Invalid session."}
```

``` http
HTTP/1.0 406 Not Acceptable
Server: temboard-agent/0.0.1 Python/2.7.8
Date: Wed, 22 Apr 2015 09:58:00 GMT
Content-type: application/json

{"error": "Parameter 'action' is malformed."}
```

## Activity plugin API {#activity_api}

> Get list of PostgreSQL backends.
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed.

**Example request**:

``` http
GET /activity HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/0.0.1 Python/2.7.8
Date: Wed, 22 Apr 2015 09:57:52 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

{
    "rows":
    [
        {
            "pid": 6285,
            "database": "postgres",
            "user": "postgres",
            "client": null,
            "cpu": 0.0,
            "memory": 0.13,
            "read_s": "0.00B",
            "write_s": "0.00B",
            "iow": "N",
            "wait": "N",
            "duration": "1.900",
            "state": "idle",
            "query": "SELECT 1;"
        }
    ]
}
```

**Error responses**:

``` http
HTTP/1.0 401 Unauthorized
Server: temboard-agent/0.0.1 Python/2.7.8
Date: Wed, 22 Apr 2015 09:58:00 GMT
Content-type: application/json

{"error": "Invalid session."}
```

``` http
HTTP/1.0 406 Not Acceptable
Server: temboard-agent/0.0.1 Python/2.7.8
Date: Wed, 22 Apr 2015 09:58:00 GMT
Content-type: application/json

{"error": "Parameter 'X-Session' is malformed."}
```

> Get list of PostgreSQL backends waiting for lock acquisition.
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed.

**Example request**:

``` http
GET /activity/waiting HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/0.0.1 Python/2.7.8
Date: Wed, 22 Apr 2015 09:57:52 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

{
    "rows":
    [
        {
            "pid": 13532,
            "database": "test",
            "user": "postgres",
            "cpu": 0.0,
            "memory": 0.16,
            "read_s": "0.00B",
            "write_s": "0.00B",
            "iow": "N",
            "relation": " ",
            "type": "transactionid",
            "mode": "ShareLock",
            "state": "active",
            "duration": 4.35,
            "query": "DELETE FROM t1 WHERE id = 1;"
        }
    ]
}
```

> Get list of PostgreSQL backends blocking other backends due to lock
> acquisition.
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed.

**Example request**:

``` http
GET /activity/blocking HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/0.0.1 Python/2.7.8
Date: Wed, 22 Apr 2015 09:57:52 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

{
    "rows":
    [
        {
            "pid": 13309,
            "database": "test",
            "user": "postgres",
            "cpu": 0.0,
            "memory": 0.2,
            "read_s": "0.00B",
            "write_s": "0.00B",
            "iow": "N",
            "relation": " ",
            "type": "transactionid",
            "mode": "ExclusiveLock",
            "state": "idle in transaction",
            "duration": 4126.98,
            "query": "UPDATE t1 SET id = 100000000 where id =1;"
        }
    ]
}
```

> Terminate (kill) a list of PostgreSQL backends.
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed.

**Example request**:

``` http
POST /activity/kill HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
Content-Type: application/json

{
    "pids":
    [
        13309
    ]
}
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/0.0.1 Python/2.7.8
Date: Wed, 22 Apr 2015 09:57:52 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

{
    "backends":
    [
        {"pid": 13309, "killed": true},
    ]
}
```

## Dashboard plugin API {#dashboard_api}

> Get the whole last data set used to render dashboard view. Data have
> been collected async.
>
> query key
>
> :   Agent\'s key for authentication (optional)
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed.

``` http
GET /dashboard HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/0.0.1 Python/2.7.8
Date: Wed, 22 Apr 2015 09:57:52 GMT
Content-type: application/json

{
    "active_backends":
    {
        "nb": 1,
        "time": 1429617751.29224
    },
    "loadaverage": 0.28,
    "os_version": "Linux 3.16.0-34-generic x86_64",
    "pg_version": "9.4.1",
    "n_cpu": "4",
    "hitratio": 98.0,
    "databases":
    {
        "total_size": "1242 MB",
        "time": "14:02",
        "databases": 4,
        "total_commit": 16728291,
        "total_rollback": 873
    },
    "memory": {
        "total": 3950660,
        "active": 46.9,
        "cached": 20.2,
        "free": 32.9
    },
    "hostname": "neptune",
    "cpu":
    {
        "iowait": 0.0,
        "idle": 97.5,
        "steal": 0.0,
        "user": 2.5,
        "system": 0.0
    },
    "buffers":
    {
        "nb": 348247,
        "time": 1429617751.276508
    }
}
```

**Error responses**:

``` http
HTTP/1.0 401 Unauthorized
Server: temboard-agent/0.0.1 Python/2.7.8
Date: Wed, 22 Apr 2015 09:58:00 GMT
Content-type: application/json

{"error": "Invalid session."}
```

``` http
HTTP/1.0 406 Not Acceptable
Server: temboard-agent/0.0.1 Python/2.7.8
Date: Wed, 22 Apr 2015 09:58:00 GMT
Content-type: application/json

{"error": "Parameter 'X-Session' is malformed."}
```

> Get the dashboard plugin config.
>
> query key
>
> :   Agent\'s key for authentication (optional)
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed.

``` http
GET /dashboard HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/0.0.1 Python/2.7.8
Date: Wed, 22 Apr 2015 09:57:52 GMT
Content-type: application/json

{
    "history_length": 150,
    "scheduler_interval": 2
}
```

**Error responses**:

``` http
HTTP/1.0 401 Unauthorized
Server: temboard-agent/0.0.1 Python/2.7.8
Date: Wed, 22 Apr 2015 09:58:00 GMT
Content-type: application/json

{"error": "Invalid session."}
```

``` http
HTTP/1.0 406 Not Acceptable
Server: temboard-agent/0.0.1 Python/2.7.8
Date: Wed, 22 Apr 2015 09:58:00 GMT
Content-type: application/json

{"error": "Parameter 'X-Session' is malformed."}
```

> Synchronous version of `/dashboard`. Please refer to `/dashboard` API
> documentation for details.

> Get the last `n` sets of dashboard data. `n` is defined by parameter
> `history_length` from the `dashboard` section of configuration file.
> Default value is `150`.
>
> query key
>
> :   Agent\'s key for authentication (optional)
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed.

``` http
GET /dashboard/history HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/0.0.1 Python/2.7.12
Date: Thu, 20 Apr 2017 15:56:56 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

[
    {
        "active_backends":
        {
            "nb": 1,
            "time": 1492703660.798522
        },
        "max_connections": 100,
        "databases":
        {
            "total_rollback": 1081,
            "total_size": "158 MB",
            "timestamp": 1492703660.913077,
            "time": "17:54",
            "total_commit": 2825374,
            "databases": 6
        },
        "hostname": "poseidon.home.priv",
        "pg_version": "PostgreSQL 9.5.5 on x86_64-pc-linux-gnu, compiled by x86_64-pc-linux-gnu-gcc (Gentoo 4.9.4 p1.0, pie-0.6.4) 4.9.4, 64-bit",
        "memory":
        {
            "active": 51.0,
            "cached": 29.5,
            "total": 8082124,
            "free": 19.5
        },
        "cpu":
        {
            "iowait": 0.0,
            "idle": 100.0,
            "steal": 0.0,
            "user": 0.0,
            "system": 0.0
        },
        "os_version": "Linux 4.9.6-gentoo-r1",
        "loadaverage": 0.18,
        "hitratio": 99.0,
        "pg_uptime": "01:50:31.573788",
        "pg_port": "5432",
        "n_cpu": 4,
        "pg_data": "/var/lib/postgresql/9.5/data",
        "buffers":
        {
            "nb": 27670,
            "time": 1492703660.784254
        }
    }
]
```

> Get the number of buffers allocated by PostgreSQL `background writer`
> process.
>
> query key
>
> :   Agent\'s key for authentication (optional)
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed.

``` http
GET /dashboard/buffers HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/0.0.1 Python/2.7.12
Date: Thu, 20 Apr 2017 16:09:58 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

{"buffers": {"nb": 27696, "time": 1492704598.784161}}
```

> Get PostgreSQL global cache hit ratio.
>
> query key
>
> :   Agent\'s key for authentication (optional)
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed.

``` http
GET /dashboard/hitratio HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/0.0.1 Python/2.7.12
Date: Thu, 20 Apr 2017 16:28:33 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

{"hitratio": 99.0}
```

> Get the total number of active backends.
>
> query key
>
> :   Agent\'s key for authentication (optional)
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed.

``` http
GET /dashboard/active_backends HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/0.0.1 Python/2.7.12
Date: Thu, 20 Apr 2017 16:35:55 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

{
    "active_backends":
    {
        "nb": 1,
        "time": 1492706155.986045
    }
}
```

> Get CPU usage.
>
> query key
>
> :   Agent\'s key for authentication (optional)
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed.

``` http
GET /dashboard/cpu HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/0.0.1 Python/2.7.12
Date: Thu, 20 Apr 2017 16:40:46 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

{
    "cpu":
    {
        "iowait": 0.0,
        "idle": 100.0,
        "steal": 0.0,
        "user": 0.0,
        "system": 0.0
    }
}
```

> System loadaverage.
>
> query key
>
> :   Agent\'s key for authentication (optional)
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed.

``` http
GET /dashboard/loadaverage HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/0.0.1 Python/2.7.12
Date: Thu, 20 Apr 2017 16:44:04 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

{
    "loadaverage": 0.06
}
```

> Memory usage.
>
> query key
>
> :   Agent\'s key for authentication (optional)
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed.

``` http
GET /dashboard/memory HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/0.0.1 Python/2.7.12
Date: Thu, 20 Apr 2017 16:46:39 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

{
    "memory":
    {
        "active": 50.1,
        "cached": 29.5,
        "total": 8082124,
        "free": 20.4
    }
}
```

> Machine hostname.
>
> query key
>
> :   Agent\'s key for authentication (optional)
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed.

``` http
GET /dashboard/hostname HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/0.0.1 Python/2.7.12
Date: Thu, 20 Apr 2017 16:48:49 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

{
    "hostname": "poseidon.home.priv"
}
```

> Operating system version.
>
> query key
>
> :   Agent\'s key for authentication (optional)
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed.

``` http
GET /dashboard/os_version HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/0.0.1 Python/2.7.12
Date: Thu, 20 Apr 2017 16:55:44 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

{
    "os_version": "Linux 4.9.6-gentoo-r1"
}
```

> Get PostgreSQL server version.
>
> query key
>
> :   Agent\'s key for authentication (optional)
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed.

``` http
GET /dashboard/pg_version HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/0.0.1 Python/2.7.12
Date: Thu, 20 Apr 2017 16:59:26 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

{
    "pg_version": "PostgreSQL 9.5.5 on x86_64-pc-linux-gnu, compiled by x86_64-pc-linux-gnu-gcc (Gentoo 4.9.4 p1.0, pie-0.6.4) 4.9.4, 64-bit"
}
```

> Number of CPU.
>
> query key
>
> :   Agent\'s key for authentication (optional)
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed.

``` http
GET /dashboard/n_cpu HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/0.0.1 Python/2.7.12
Date: Thu, 20 Apr 2017 17:03:55 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

{
    "n_cpu": 4
}
```

> PostgreSQL cluster size & number of databases.
>
> query key
>
> :   Agent\'s key for authentication (optional)
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed.

``` http
GET /dashboard/databases HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/0.0.1 Python/2.7.12
Date: Thu, 20 Apr 2017 17:08:59 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

{
    "databases":
    {
        "total_rollback": 1087,
        "total_size": "159 MB",
        "timestamp": 1492708139.981268,
        "databases": 6,
        "total_commit": 2848707,
        "time": "19:08"
    }
}
```

> Get a bunch of global informations about system and PostgreSQL.
>
> query key
>
> :   Agent\'s key for authentication (optional)
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed.

``` http
GET /dashboard/info HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/0.0.1 Python/2.7.12
Date: Thu, 20 Apr 2017 17:17:57 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

{
    "hostname": "poseidon.home.priv",
    "os_version": "Linux 4.9.6-gentoo-r1",
    "pg_port": "5432",
    "pg_uptime": "03:14:08.029574",
    "pg_version": "PostgreSQL 9.5.5 on x86_64-pc-linux-gnu, compiled by x86_64-pc-linux-gnu-gcc (Gentoo 4.9.4 p1.0, pie-0.6.4) 4.9.4, 64-bit",
    "pg_data": "/var/lib/postgresql/9.5/data"
}
```

> Get the max_connections settings value.
>
> query key
>
> :   Agent\'s key for authentication (optional)
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed.

``` http
GET /dashboard/active_backends HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/0.0.1 Python/2.7.12
Date: Thu, 20 Apr 2017 16:35:55 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

{
    "max_connections": 100
}
```

## Monitoring plugin API {#monitoring_api}

> Run `sessions` monitoring probe.
>
> query key
>
> :   Agent\'s key for authentication (optional)
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed.

**Example request**:

``` http
GET /monitoring/probe/sessions HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/0.0.1 Python/2.7.12
Date: Fri, 21 Apr 2017 06:24:45 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

{
    "sessions":
    [
        {
            "idle_in_xact": 0,
            "idle_in_xact_aborted": 0,
            "no_priv": 0,
            "idle": 0,
            "datetime": "2017-04-21 08:24:45.003511+02",
            "disabled": 0,
            "waiting": 0,
            "port": 5432,
            "active": 0,
            "dbname": "temboard_test",
            "fastpath": 0
        }
    ]
}
```

**Error responses**:

``` http
HTTP/1.0 401 Unauthorized
Server: temboard-agent/0.0.1 Python/2.7.8
Date: Wed, 22 Apr 2015 09:58:00 GMT
Content-type: application/json

{"error": "Invalid session."}
```

``` http
HTTP/1.0 406 Not Acceptable
Server: temboard-agent/0.0.1 Python/2.7.8
Date: Wed, 22 Apr 2015 09:58:00 GMT
Content-type: application/json

{"error": "Parameter 'X-Session' is malformed."}
```

> Run `xacts` monitoring probe.
>
> query key
>
> :   Agent\'s key for authentication (optional)
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed.

**Example request**:

``` http
GET /monitoring/probe/xacts HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/0.0.1 Python/2.7.12
Date: Fri, 21 Apr 2017 06:24:45 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

{
    "xacts":
    [
        {
            "port": 5432,
            "n_commit": 0,
            "n_rollback": 0,
            "dbname": "template1",
            "datetime": "2017-04-21 08:42:12.092111+02"
        }
    ]
}
```

> Run `locks` monitoring probe.
>
> query key
>
> :   Agent\'s key for authentication (optional)
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed.

**Example request**:

``` http
GET /monitoring/probe/locks HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/0.0.1 Python/2.7.12
Date: Fri, 21 Apr 2017 06:24:45 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

{
    "locks":
    [
        {
            "exclusive": 0,
            "waiting_share_row_exclusive": 0,
            "waiting_share": 0,
            "row_share": 0,
            "waiting_row_exclusive": 0,
            "share_row_exclusive": 0,
            "port": 5432,
            "share": 0,
            "waiting_access_share": 0,
            "dbname": "test",
            "row_exclusive": 0,
            "share_update_exclusive": 0,
            "access_share": 0,
            "access_exclusive": 0,
            "waiting_exclusive": 0,
            "siread": 0,
            "datetime": "2017-04-21 08:55:11.768602+02",
            "waiting_share_update_exclusive": 0,
            "waiting_row_share": 0,
            "waiting_access_exclusive": 0
        }
    ]
}
```

> Run `blocks` monitoring probe.
>
> query key
>
> :   Agent\'s key for authentication (optional)
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed.

**Example request**:

``` http
GET /monitoring/probe/blocks HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/0.0.1 Python/2.7.12
Date: Fri, 21 Apr 2017 06:24:45 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

{
    "blocks":
    [
        {
            "blks_read": 382,
            "dbname": "postgres",
            "hitmiss_ratio": 99.9998294969873,
            "blks_hit": 224042580,
            "datetime": "2017-04-21 08:57:32.11277+02",
            "port": 5432
        }
    ]
}
```

> Run `bgwriter` monitoring probe.
>
> query key
>
> :   Agent\'s key for authentication (optional)
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed.

**Example request**:

``` http
GET /monitoring/probe/bgwriter HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/0.0.1 Python/2.7.12
Date: Fri, 21 Apr 2017 06:24:45 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

{
    "bgwriter":
    [
        {
            "checkpoint_write_time": 15113301.0,
            "checkpoints_timed": 1960,
            "buffers_alloc": 29369,
            "buffers_clean": 0,
            "buffers_backend_fsync": 0,
            "checkpoint_sync_time": 177464.0,
            "checkpoints_req": 0,
            "port": 5432,
            "buffers_backend": 42258,
            "maxwritten_clean": 0,
            "datetime": "2017-04-21 08:59:20.171443+02",
            "buffers_checkpoint": 149393,
            "stats_reset": "2017-04-14 13:37:15.288701+02"
        }
    ]
}
```

> Run `db_size` monitoring probe.
>
> query key
>
> :   Agent\'s key for authentication (optional)
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed.

**Example request**:

``` http
GET /monitoring/probe/db_size HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/0.0.1 Python/2.7.12
Date: Fri, 21 Apr 2017 06:24:45 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

{
    "db_size":
    [
        {
            "port": 5432,
            "size": 7021060,
            "dbname": "template1",
            "datetime": "2017-04-21 09:00:47.528365+02"
        },
        {
            "port": 5432,
            "size": 7168172,
            "dbname": "postgres",
            "datetime": "2017-04-21 09:00:47.528365+02"
        }
    ]
}
```

> Run `tblspc_size` monitoring probe.
>
> query key
>
> :   Agent\'s key for authentication (optional)
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed.

**Example request**:

``` http
GET /monitoring/probe/tblspc_size HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/0.0.1 Python/2.7.12
Date: Fri, 21 Apr 2017 06:24:45 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

{
    "tblspc_size":
    [
        {
            "size": 181067120,
            "port": 5432,
            "spcname": "pg_default",
            "datetime": "2017-04-21 09:13:55.196718+02"
        },
        {
            "size": 622400,
            "port": 5432,
            "spcname": "pg_global",
            "datetime": "2017-04-21 09:13:55.196718+02"
        },
        {
            "size": null,
            "port": 5432,
            "spcname": "tbs",
            "datetime": "2017-04-21 09:13:55.196718+02"
        }
    ]
}
```

> Run `filesystems_size` monitoring probe.
>
> query key
>
> :   Agent\'s key for authentication (optional)
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed.

**Example request**:

``` http
GET /monitoring/probe/filesystems_size HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/0.0.1 Python/2.7.12
Date: Fri, 21 Apr 2017 06:24:45 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

{
    "filesystems_size":
    [
        {
            "device": "udev",
            "total": 10485760,
            "mount_point": "/dev",
            "used": 4096,
            "datetime": "2017-04-21 07:16:25 +0000"
        },
        {
            "device": "/dev/sda4",
            "total": 21003628544,
            "mount_point": "/",
            "used": 11889070080,
            "datetime": "2017-04-21 07:16:25 +0000"
        }
    ]
}
```

> Run `cpu` monitoring probe.
>
> query key
>
> :   Agent\'s key for authentication (optional)
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed.

**Example request**:

``` http
GET /monitoring/probe/cpu HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/0.0.1 Python/2.7.12
Date: Fri, 21 Apr 2017 06:24:45 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

{
    "cpu":
    [
        {
            "time_system": 140,
            "time_steal": 0,
            "time_iowait": 10,
            "datetime": "2017-04-21 08:09:27 +0000",
            "measure_interval": 27.88518500328064,
            "time_idle": 27410,
            "cpu": "cpu0",
            "time_user": 290
        },
        {
            "time_system": 110,
            "time_steal": 0,
            "time_iowait": 10,
            "datetime": "2017-04-21 08:09:27 +0000",
            "measure_interval": 27.885642051696777,
            "time_idle": 27410,
            "cpu": "cpu1",
            "time_user": 290
        },
        {
            "time_system": 170,
            "time_steal": 0,
            "time_iowait": 1390,
            "datetime": "2017-04-21 08:09:27 +0000",
            "measure_interval": 27.885895013809204,
            "time_idle": 26040,
            "cpu": "cpu2",
            "time_user": 220
        },
        {
            "time_system": 130,
            "time_steal": 0,
            "time_iowait": 20,
            "datetime": "2017-04-21 08:09:27 +0000",
            "measure_interval": 27.88606309890747,
            "time_idle": 27370,
            "cpu": "cpu3",
            "time_user": 320
        }
    ]
}
```

> Run `process` monitoring probe.
>
> query key
>
> :   Agent\'s key for authentication (optional)
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed.

**Example request**:

``` http
GET /monitoring/probe/process HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/0.0.1 Python/2.7.12
Date: Fri, 21 Apr 2017 06:24:45 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

{
    "process":
    [
        {
            "measure_interval": 55.731096029281616,
            "procs_total": "486",
            "forks": 165,
            "procs_blocked": 0,
            "context_switches": 31453,
            "procs_running": 4,
            "datetime": "2017-04-21 08:13:56 +0000"
        }
    ]
}
```

> Run `memory` monitoring probe.
>
> query key
>
> :   Agent\'s key for authentication (optional)
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed.

**Example request**:

``` http
GET /monitoring/probe/memory HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/0.0.1 Python/2.7.12
Date: Fri, 21 Apr 2017 06:24:45 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

{
    "memory":
    [
        {
            "mem_used": 7268151296,
            "swap_used": 0,
            "swap_total": 4026527744,
            "mem_total": 8276094976,
            "mem_cached": 2464796672,
            "mem_free": 1007943680,
            "mem_buffers": 558067712,
            "datetime": "2017-04-21 08:15:06 +0000"
        }
    ]
}
```

> Run `loadavg` monitoring probe.
>
> query key
>
> :   Agent\'s key for authentication (optional)
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed.

**Example request**:

``` http
GET /monitoring/probe/loadavg HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/0.0.1 Python/2.7.12
Date: Fri, 21 Apr 2017 06:24:45 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

{
    "loadavg":
    [
        {
            "load1": "0.07",
            "load15": "0.09",
            "load5": "0.16",
            "datetime": "2017-04-21 08:16:16 +0000"
        }
    ]
}
```

> Run `wal_files` monitoring probe.
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed.

**Example request**:

``` http
GET /monitoring/probe/wal_files HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/0.0.1 Python/2.7.12
Date: Fri, 21 Apr 2017 06:24:45 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

{
    "wal_files":
    [
        {
            "archive_ready": 0,
            "total_size": 201326592.0,
            "written_size": 13648,
            "datetime": "2017-04-21 08:17:12 +0000",
            "measure_interval": 9.273101091384888,
            "current_location": "53/700035B0",
            "total": 12,
            "port": 5432
        }
    ]
}
```

## PgConf plugin API {#pgconf_api}

> Get PostgreSQL settings from `pg_settings` system view and
> configuration files.
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed.

**Example request**:

``` http
GET /pgconf/configuration HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/0.0.1 Python/2.7.8
Date: Wed, 22 Apr 2015 09:57:52 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

[
    {
        "category": "Autovacuum",
        "rows":
        [
            {
                "context": "sighup",
                "enumvals": null,
                "max_val": null,
                "vartype": "bool",
                "boot_val": "on",
                "reset_val": "on",
                "unit": null,
                "desc": "Starts the autovacuum subprocess.",
                "name": "autovacuum",
                "min_val": null,
                "setting": "off",
                "setting_raw": "off",
                "pending_restart": "f"
            }
        ]
    }
]
```

**Error responses**:

``` http
HTTP/1.0 401 Unauthorized
Server: temboard-agent/0.0.1 Python/2.7.8
Date: Wed, 22 Apr 2015 09:58:00 GMT
Content-type: application/json

{"error": "Invalid session."}
```

``` http
HTTP/1.0 406 Not Acceptable
Server: temboard-agent/0.0.1 Python/2.7.8
Date: Wed, 22 Apr 2015 09:58:00 GMT
Content-type: application/json

{"error": "Parameter 'X-Session' is malformed."}
```

> Get list of settings categories.
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed.

**Example request**:

``` http
GET /pgconf/configuration/categories HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/0.0.1 Python/2.7.8
Date: Wed, 22 Apr 2015 09:57:52 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

{
    "categories":
    [
        "Autovacuum",
        "Client Connection Defaults / Locale and Formatting",
        "Client Connection Defaults / Other Defaults"
    ]
}
```

> Update one or many PostgreSQL settings values. This API issues
> `ALTER SYSTEM` SQL statements.
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` or setting item is malformed.
>
> status 400
>
> :   invalid JSON format.

**Example request**:

``` http
POST /pgconf/configuration HTTP/1.1
Content-Type: application/json
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e

{
    "settings":
    [
        {
            "name": "autovacuum",
            "setting": "on"
        }
    ]
}
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/0.0.1 Python/2.7.8
Date: Wed, 22 Apr 2015 09:57:52 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

{
    "settings":
    [
        {
            "setting": "on",
            "restart": false,
            "name": "autovacuum",
            "previous_setting": "off"
        }
    ]
}
```

> Get list of settings for one category, based on category name.
>
> reqheader X-Session
>
> :   Session ID
>
> param category_name
>
> :   Setting category name
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed.

**Example request**:

``` http
GET /pgconf/configuration/category/Autovacuum HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/0.0.1 Python/2.7.8
Date: Wed, 22 Apr 2015 09:57:52 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

[
    {
        "category": "Autovacuum",
        "rows":
        [
            {
                "context": "sighup",
                "enumvals": null,
                "max_val": null,
                "vartype": "bool",
                "boot_val": "on",
                "reset_val": "on",
                "unit": null,
                "desc": "Starts the autovacuum subprocess. ",
                "name": "autovacuum",
                "min_val": null,
                "setting": "on",
                "setting_raw": "on",
                "pending_restart": "f"
            }
        ]
    }
]
```

> Shows settings waiting for PostgreSQL server restart
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed.

**Example request**:

``` http
GET /pgconf/configuration/status HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/0.0.1 Python/2.7.8
Date: Wed, 22 Apr 2015 09:57:52 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

{
    "restart_changes":
    [
        {
            "context": "postmaster",
            "enumvals": null,
            "max_val": 1073741823,
            "vartype": "integer",
            "boot_val": 1024,
            "reset_val": 16384,
            "unit": "8kB",
            "desc": "Sets the number of shared memory buffers used by the server. ",
            "name": "shared_buffers",
            "min_val": 16,
            "setting": 16384,
            "setting_raw": "128MB",
            "pending_restart": "t"
        }
    ],
    "restart_pending": true
}
```

## Maintenance API {#maintenance_api}

> Get information about the instance and its databases
>
> query key
>
> :   Agent\'s key for authentication (optional)
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed.

**Example request**:

``` http
GET /maintenance HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/4.0+master Python/3.7.2
Date: Fri, 22 Mar 2019 10:21:44 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

{
    "databases": [
        {
            "datname": "postgres",
            "indexes_bloat_bytes": 335872.0,
            "indexes_bloat_size": "328 kB",
            "indexes_bytes": 3162112.0,
            "indexes_size": "3088 kB",
            "n_indexes": 115.0,
            "n_tables": 69.0,
            "tables_bloat_bytes": 49152.0,
            "tables_bloat_size": "48 kB",
            "tables_bytes": 2957312.0,
            "tables_size": "2888 kB",
            "toast_bytes": 679936.0,
            "toast_size": "664 kB",
            "total_bytes": 7788007,
            "total_size": "7605 kB"
        }
    ],
    "instance": {
        "total_bytes": 7788007.0,
        "total_size": "7605 kB"
    }
}
```

> Get information about one database
>
> query key
>
> :   Agent\'s key for authentication (optional)
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed.

**Example request**:

``` http
GET /maintenance/postgres HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/4.0+master Python/3.7.2
Date: Fri, 22 Mar 2019 10:24:15 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

{
    "schemas": [
        {
            "indexes_bloat_bytes": null,
            "indexes_bloat_size": null,
            "indexes_bytes": 0,
            "indexes_size": null,
            "n_indexes": 0,
            "n_tables": 7,
            "name": "information_schema",
            "tables_bloat_bytes": 0.0,
            "tables_bloat_size": "0 bytes",
            "tables_bytes": 98304,
            "tables_size": "96 kB",
            "toast_bytes": 57344.0,
            "toast_size": "56 kB",
            "total_bytes": 352256,
            "total_size": "344 kB"
        },
        {
            "indexes_bloat_bytes": 335872.0,
            "indexes_bloat_size": "328 kB",
            "indexes_bytes": 3219456,
            "indexes_size": "3144 kB",
            "n_indexes": 115,
            "n_tables": 62,
            "name": "pg_catalog",
            "tables_bloat_bytes": 49152.0,
            "tables_bloat_size": "48 kB",
            "tables_bytes": 2940928,
            "tables_size": "2872 kB",
            "toast_bytes": 630784.0,
            "toast_size": "616 kB",
            "total_bytes": 8003584,
            "total_size": "7816 kB"
        },
        {
            "indexes_bloat_bytes": 16384.0,
            "indexes_bloat_size": "16 kB",
            "indexes_bytes": 180224,
            "indexes_size": "176 kB",
            "n_indexes": 3,
            "n_tables": 3,
            "name": "public",
            "tables_bloat_bytes": 16384.0,
            "tables_bloat_size": "16 kB",
            "tables_bytes": 352256,
            "tables_size": "344 kB",
            "toast_bytes": 24576.0,
            "toast_size": "24 kB",
            "total_bytes": 557056,
            "total_size": "544 kB"
        }
    ],
    "total_bytes": 8492519,
    "total_size": "8293 kB"
}
```

> Get information about one schema
>
> query key
>
> :   Agent\'s key for authentication (optional)
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed.

**Example request**:

``` http
GET /maintenance/postgres/schema/public HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/4.0+master Python/3.7.2
Date: Fri, 22 Mar 2019 10:38:45 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

{
    "indexes": [
        {
            "bloat_bytes": 8192.0,
            "bloat_size": "8192 bytes",
            "def": "CREATE UNIQUE INDEX city_pkey ON public.city USING btree (id)",
            "idx_tup_fetch": 0,
            "idx_tup_read": 0,
            "indexrelname": "city_pkey",
            "indisunique": true,
            "name": "city_pkey",
            "number_of_columns": 1,
            "scans": 0,
            "tablename": "city",
            "tablespace": null,
            "total_bytes": 114688,
            "total_size": "112 kB",
            "type": "btree"
        },
        {
            "bloat_bytes": 0.0,
            "bloat_size": "0 bytes",
            "def": "CREATE UNIQUE INDEX country_pkey ON public.country USING btree (code)",
            "idx_tup_fetch": 0,
            "idx_tup_read": 0,
            "indexrelname": "country_pkey",
            "indisunique": true,
            "name": "country_pkey",
            "number_of_columns": 1,
            "scans": 0,
            "tablename": "country",
            "tablespace": null,
            "total_bytes": 16384,
            "total_size": "16 kB",
            "type": "btree"
        },
        {
            "bloat_bytes": 8192.0,
            "bloat_size": "8192 bytes",
            "def": "CREATE UNIQUE INDEX countrylanguage_pkey ON public.countrylanguage USING btree (countrycode, language)",
            "idx_tup_fetch": 0,
            "idx_tup_read": 0,
            "indexrelname": "countrylanguage_pkey",
            "indisunique": true,
            "name": "countrylanguage_pkey",
            "number_of_columns": 2,
            "scans": 0,
            "tablename": "countrylanguage",
            "tablespace": null,
            "total_bytes": 49152,
            "total_size": "48 kB",
            "type": "btree"
        }
    ],
    "size": "544 kB",
    "tables": [
        {
            "bloat_bytes": 16384.0,
            "bloat_size": "16 kB",
            "index_bloat_bytes": 8192.0,
            "index_bloat_size": "8192 bytes",
            "index_bytes": 114688,
            "index_size": "112 kB",
            "n_indexes": 1,
            "name": "city",
            "row_estimate": 4079.0,
            "table_bytes": 262144,
            "table_size": "256 kB",
            "toast_bytes": 8192,
            "toast_size": "8192 bytes",
            "total_bytes": 385024,
            "total_size": "376 kB"
        },
        {
            "bloat_bytes": 0.0,
            "bloat_size": "0 bytes",
            "index_bloat_bytes": 0.0,
            "index_bloat_size": "0 bytes",
            "index_bytes": 16384,
            "index_size": "16 kB",
            "n_indexes": 1,
            "name": "country",
            "row_estimate": 239.0,
            "table_bytes": 40960,
            "table_size": "40 kB",
            "toast_bytes": 8192,
            "toast_size": "8192 bytes",
            "total_bytes": 65536,
            "total_size": "64 kB"
        },
        {
            "bloat_bytes": 0.0,
            "bloat_size": "0 bytes",
            "index_bloat_bytes": 8192.0,
            "index_bloat_size": "8192 bytes",
            "index_bytes": 49152,
            "index_size": "48 kB",
            "n_indexes": 1,
            "name": "countrylanguage",
            "row_estimate": 984.0,
            "table_bytes": 49152,
            "table_size": "48 kB",
            "toast_bytes": 8192,
            "toast_size": "8192 bytes",
            "total_bytes": 106496,
            "total_size": "104 kB"
        }
    ],
    "total_bytes": 557056
}
```

> Get information about one table
>
> query key
>
> :   Agent\'s key for authentication (optional)
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed.

**Example request**:

``` http
GET /maintenance/postgres/schema/public/table/country HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/4.0+master Python/3.7.2
Date: Fri, 22 Mar 2019 10:40:48 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

{
    "analyze_count": 1,
    "autoanalyze_count": 1,
    "autovacuum_count": 0,
    "bloat_bytes": 0.0,
    "bloat_size": "0 bytes",
    "fillfactor": 100,
    "idx_scan": 0,
    "idx_tup_fetch": 0,
    "index_bloat_bytes": 0.0,
    "index_bloat_size": "0 bytes",
    "index_bytes": 16384,
    "index_size": "16 kB",
    "indexes": [
        {
            "bloat_bytes": 0.0,
            "bloat_size": "0 bytes",
            "def": "CREATE UNIQUE INDEX country_pkey ON public.country USING btree (code)",
            "idx_tup_fetch": 0,
            "idx_tup_read": 0,
            "indexrelname": "country_pkey",
            "indisunique": true,
            "name": "country_pkey",
            "number_of_columns": 1,
            "scans": 0,
            "tablename": "country",
            "tablespace": null,
            "total_bytes": 16384,
            "total_size": "16 kB",
            "type": "btree"
        }
    ],
    "last_analyze": "2019-03-22 10:37:19.577101+00",
    "last_autoanalyze": "2019-03-22 10:37:44.297278+00",
    "last_autovacuum": null,
    "last_vacuum": null,
    "n_dead_tup": 0,
    "n_live_tup": 239,
    "n_mod_since_analyze": 0,
    "n_tup_del": 0,
    "n_tup_hot_upd": 0,
    "n_tup_ins": 239,
    "n_tup_upd": 0,
    "name": "country",
    "relid": "16432",
    "relname": "country",
    "row_estimate": 239.0,
    "schemaname": "public",
    "seq_scan": 3,
    "seq_tup_read": 717,
    "table_bytes": 40960,
    "table_size": "40 kB",
    "toast_bytes": 8192,
    "toast_size": "8192 bytes",
    "total_bytes": 65536,
    "total_size": "64 kB",
    "vacuum_count": 0
}
```

> Launch a VACUUM on the database
>
> The VACUUM can be scheduled if [datetime]{.title-ref} is provided.
>
> The mode parameter can be a combination of \'full\', \'freeze\' or
> \'analyze\'.
>
> query key
>
> :   Agent\'s key for authentication (optional)
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed, Parameter \'mode\' is malformed
>     or Parameter \'datetime\' is maformed.

**Example request**:

``` http
POST /maintenance/postgres/vacuum HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
Content-type: application/json

{
    "mode": "full,analyze",
    "datetime": "2019-03-22T12:24:39Z"
}
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/4.0+master Python/3.7.2
Date: Fri, 22 Mar 2019 11:08:02 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

{
    "id": "239cd9a0"
}
```

> Launch a VACUUM on the table.
>
> The VACUUM can be scheduled if [datetime]{.title-ref} is provided.
>
> The mode parameter can be a combination of \'full\', \'freeze\' or
> \'analyze\'.
>
> query key
>
> :   Agent\'s key for authentication (optional)
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed, Parameter \'mode\' is malformed
>     or Parameter \'datetime\' is maformed.

**Example request**:

``` http
POST /maintenance/postgres/schema/public/table/country/vacuum HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
Content-type: application/json

{
    "mode": "full,analyze",
    "datetime": "2019-03-22T12:24:39Z"
}
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/4.0+master Python/3.7.2
Date: Fri, 22 Mar 2019 11:08:02 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

{
    "id": "229cc880"
}
```

> Get the id of the scheduled VACUUM operations for the given table.
>
> query key
>
> :   Agent\'s key for authentication (optional)
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed.

**Example request**:

``` http
GET /maintenance/postgres/schema/public/table/country/vacuum/scheduled HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/4.0+master Python/3.7.2
Date: Fri, 22 Mar 2019 14:39:01 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

[
    {
        "datetime": "2019-03-23T11:28:00Z",
        "dbname": "postgres",
        "id": "9ce6426b",
        "index": null,
        "mode": "full",
        "schema": "public",
        "status": "todo",
        "table": "country"
    }
]
```

> Cancel the given VACUUM operation.
>
> query key
>
> :   Agent\'s key for authentication (optional)
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed.

**Example request**:

``` http
DELETE /maintenance/vacuum/9ce6426b HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/4.0+master Python/3.7.2
Date: Fri, 22 Mar 2019 15:01:01 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

{"response": "ok"}
```

> Get the id of all the scheduled VACUUM operations.
>
> query key
>
> :   Agent\'s key for authentication (optional)
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed.

**Example request**:

``` http
GET /maintenance/vacuum/scheduled HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/4.0+master Python/3.7.2
Date: Fri, 22 Mar 2019 14:39:01 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

[
    {
        "datetime": "2019-03-23T11:28:00Z",
        "dbname": "postgres",
        "id": "9ce6426b",
        "index": null,
        "mode": "full",
        "schema": "public",
        "status": "todo",
        "table": "country"
    },
    {
        "datetime": "2019-03-23T11:28:00Z",
        "dbname": "postgres",
        "id": "785b82c6",
        "index": null,
        "mode": "full",
        "schema": "public",
        "status": "todo",
        "table": "city"
    }
]
```

> Get the id of all the scheduled VACUUM operations.
>
> query key
>
> :   Agent\'s key for authentication (optional)
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed.

**Example request**:

``` http
GET /maintenance/postgres/vacuum/scheduled HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/4.0+master Python/3.7.2
Date: Fri, 22 Mar 2019 14:39:01 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

[
    {
        "datetime": "2019-03-23T11:28:00Z",
        "dbname": "postgres",
        "id": "9ce6426b",
        "index": null,
        "mode": "full",
        "schema": "public",
        "status": "todo",
        "table": "country"
    },
    {
        "datetime": "2019-03-23T11:28:00Z",
        "dbname": "postgres",
        "id": "785b82c6",
        "index": null,
        "mode": "full",
        "schema": "public",
        "status": "todo",
        "table": "city"
    }
]
```

> Launch a ANALYZE on the database.
>
> The ANALYZE can be scheduled if [datetime]{.title-ref} is provided.
>
> query key
>
> :   Agent\'s key for authentication (optional)
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed, Parameter \'datetime\' is
>     maformed.

**Example request**:

``` http
POST /maintenance/postgres/analyze HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
Content-type: application/json

{
    "datetime": "2019-03-23T11:28:00Z"
}
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/4.0+master Python/3.7.2
Date: Fri, 22 Mar 2019 15:12:02 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

{
    "id": "1ac59a5e"
}
```

> Launch a ANALYZE on the table.
>
> The ANALYZE can be scheduled if [datetime]{.title-ref} is provided.
>
> query key
>
> :   Agent\'s key for authentication (optional)
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed, Parameter \'datetime\' is
>     maformed.

**Example request**:

``` http
POST /maintenance/postgres/schema/public/table/country/analyze HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
Content-type: application/json

{
    "datetime": "2019-03-23T11:28:00Z"
}
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/4.0+master Python/3.7.2
Date: Fri, 22 Mar 2019 15:12:02 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

{
    "id": "1045055e"
}
```

> Get the id of the scheduled ANALYZE operations for the given database
>
> query key
>
> :   Agent\'s key for authentication (optional)
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed.

**Example request**:

``` http
GET /maintenance/postgres/analyze/scheduled HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/4.0+master Python/3.7.2
Date: Fri, 22 Mar 2019 14:39:01 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

[
    {
        "datetime": "2019-03-23T11:28:00Z",
        "dbname": "postgres",
        "id": "1045055e",
        "index": null,
        "mode": null,
        "schema": "public",
        "status": "todo",
        "table": "country"
    }
]
```

> Get the id of the scheduled ANALYZE operations for the given table.
>
> query key
>
> :   Agent\'s key for authentication (optional)
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed.

**Example request**:

``` http
GET /maintenance/postgres/schema/public/table/country/analyze/scheduled HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/4.0+master Python/3.7.2
Date: Fri, 22 Mar 2019 14:39:01 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

[
    {
        "datetime": "2019-03-23T11:28:00Z",
        "dbname": "postgres",
        "id": "1045055e",
        "index": null,
        "mode": null,
        "schema": "public",
        "status": "todo",
        "table": "country"
    }
]
```

> Cancel the given ANALYZE operation.
>
> query key
>
> :   Agent\'s key for authentication (optional)
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed.

**Example request**:

``` http
DELETE /maintenance/analyze/1045055e HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/4.0+master Python/3.7.2
Date: Fri, 22 Mar 2019 15:01:01 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

{"response": "ok"}
```

> Get the id of all the scheduled ANALYZE operations.
>
> query key
>
> :   Agent\'s key for authentication (optional)
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed.

**Example request**:

``` http
GET /maintenance/analyze/scheduled HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/4.0+master Python/3.7.2
Date: Fri, 22 Mar 2019 14:39:01 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

[
    {
        "datetime": "2019-03-23T11:28:00Z",
        "dbname": "postgres",
        "id": "1847795b",
        "index": null,
        "mode": null,
        "schema": "public",
        "status": "todo",
        "table": "country"
    },
    {
        "datetime": "2019-03-23T11:28:00Z",
        "dbname": "postgres",
        "id": "1045055e",
        "index": null,
        "mode": null,
        "schema": "public",
        "status": "todo",
        "table": "city"
    }
]
```

> Launch a REINDEX on the database.
>
> The REINDEX can be scheduled if [datetime]{.title-ref} is provided.
>
> query key
>
> :   Agent\'s key for authentication (optional)
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed, Parameter \'datetime\' is
>     maformed.

**Example request**:

``` http
POST /maintenance/postgres/reindex HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
Content-type: application/json

{
    "datetime": "2019-03-22T12:24:39Z"
}
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/4.0+master Python/3.7.2
Date: Fri, 22 Mar 2019 11:08:02 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

{
    "id": "7f377004"
}
```

> Launch a REINDEX on the table.
>
> The REINDEX can be scheduled if [datetime]{.title-ref} is provided.
>
> query key
>
> :   Agent\'s key for authentication (optional)
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed, Parameter \'datetime\' is
>     maformed.

**Example request**:

``` http
POST /maintenance/postgres/schema/public/table/country/reindex HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
Content-type: application/json

{
    "datetime": "2019-03-22T12:24:39Z"
}
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/4.0+master Python/3.7.2
Date: Fri, 22 Mar 2019 11:08:02 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

{
    "id": "7f377004"
}
```

> Launch a REINDEX on the index.
>
> The REINDEX can be scheduled if [datetime]{.title-ref} is provided.
>
> query key
>
> :   Agent\'s key for authentication (optional)
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed, Parameter \'datetime\' is
>     maformed.

**Example request**:

``` http
POST /maintenance/postgres/schema/public/index/country_pkey/reindex HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
Content-type: application/json

{
    "datetime": "2019-03-22T12:24:39Z"
}
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/4.0+master Python/3.7.2
Date: Fri, 22 Mar 2019 11:08:02 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

{
    "id": "7f377004"
}
```

> Get the id of the scheduled REINDEX operations for the given database.
>
> query key
>
> :   Agent\'s key for authentication (optional)
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed.

**Example request**:

``` http
GET /maintenance/postgres/reindex/scheduled HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/4.0+master Python/3.7.2
Date: Fri, 22 Mar 2019 14:39:01 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

[
    {
        "datetime": "2019-03-23T11:28:00Z",
        "dbname": "postgres",
        "id": "7f377004",
        "index": "country_pkey",
        "mode": null,
        "schema": "public",
        "status": "todo",
        "table": null
    },
    {
        "datetime": "2019-03-24T10:32:00Z",
        "dbname": "postgres",
        "id": "7a3cae05",
        "index": null,
        "mode": null,
        "schema": null,
        "status": "todo",
        "table": null
    }
]
```

> Get the id of the scheduled REINDEX operations for the given schema.
>
> query key
>
> :   Agent\'s key for authentication (optional)
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed.

> Get the id of the scheduled REINDEX operations for the given schema.
> Alias for
> [/maintenance/\<database_name>/schema/\<schema_name>/reindex/scheduled]{.title-ref}
> (See below). Note: does not filter on table.
>
> query key
>
> :   Agent\'s key for authentication (optional)
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed.

> Get the id of the scheduled REINDEX operations for the given schema.
>
> query key
>
> :   Agent\'s key for authentication (optional)
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed.

**Example request**:

``` http
GET /maintenance/postgres/schema/public/reindex/scheduled HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/4.0+master Python/3.7.2
Date: Fri, 22 Mar 2019 14:39:01 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

[
    {
        "datetime": "2019-03-23T11:28:00Z",
        "dbname": "postgres",
        "id": "7f377004",
        "index": "country_pkey",
        "mode": null,
        "schema": "public",
        "status": "todo",
        "table": null
    }
]
```

> Cancel the given REINDEX operation.
>
> query key
>
> :   Agent\'s key for authentication (optional)
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed.

**Example request**:

``` http
DELETE /maintenance/reindex/7f377004 HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/4.0+master Python/3.7.2
Date: Fri, 22 Mar 2019 15:01:01 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

{"response": "ok"}
```

> Get the id of all the scheduled REINDEX operations.
>
> query key
>
> :   Agent\'s key for authentication (optional)
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed.

**Example request**:

``` http
GET /maintenance/reindex/scheduled HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e
```

**Example response**:

``` http
HTTP/1.0 200 OK
Server: temboard-agent/4.0+master Python/3.7.2
Date: Fri, 22 Mar 2019 14:39:01 GMT
Access-Control-Allow-Origin: *
Content-type: application/json

[
    {
        "datetime": "2019-03-23T11:28:00Z",
        "dbname": "postgres",
        "id": "7f377004",
        "index": "country_pkey",
        "mode": null,
        "schema": "public",
        "status": "todo",
        "table": null
    }
]
```

## Statements plugin API {#statements_api}

> Get latest statistics of executed SQL statements
>
> query key
>
> :   Agent\'s key for authentication (optional)
>
> reqheader X-Session
>
> :   Session ID
>
> status 200
>
> :   no error
>
> status 401
>
> :   invalid session
>
> status 404
>
> :   pg_stat_statements not enabled on the database
>
> status 500
>
> :   internal error
>
> status 406
>
> :   header `X-Session` is malformed.

**Example request**:

``` http
GET /statements HTTP/1.1
X-Session: 3b28ed94743e3ada57b217bbf9f36c6d1eb45e669a1ab693e8ca7ac3bd070b9e

{
  "snapshot_datetime": "2020-03-17 17:31:25.0929+01",
  "data": [
    {
      "rolname": "postgres",
      "datname ": "bench",
      "userid": 987342,
      "dbid": 8737,
      "queryid": 125206108,
      "query": "SELECT pg_sleep($1)",
      "calls": 1,
      "total_time": 1001.583008,
      "min_time": 1001.583008,
      "max_time": 1001.583008,
      "mean_time": 1001.583008,
      "stddev_time": 0,
      "rows": 1,
      "shared_blks_hit": 0,
      "shared_blks_read": 0,
      "shared_blks_dirtied": 0,
      "shared_blks_written": 0,
      "local_blks_hit": 0,
      "local_blks_read": 0,
      "local_blks_dirtied": 0,
      "local_blks_written": 0,
      "temp_blks_read ": 0,
      "temp_blks_written": 0,
      "blk_read_time": 0,
      "blk_write_time": 0
    }
  ]
}
```

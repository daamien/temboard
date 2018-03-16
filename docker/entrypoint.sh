#!/bin/bash -eu

command=${*-temboard-agent}

export PGHOST=${PGHOST-${TEMBOARD_HOSTNAME}}
export PGPORT=${PGPORT-5432}
export PGUSER=${PGUSER-postgres}
PGPASSWORD=${PGPASSWORD-}
export PGDATABASE=${PGDATABASE-postgres}

TEMBOARD_UI_URL=${TEMBOARD_UI_URL-}
export TEMBOARD_UI_USER=${TEMBOARD_UI_USER-admin}
export TEMBOARD_UI_PASSWORD=${TEMBOARD_UI_PASSWORD-admin}

COMPOSE_PROJECT=$(docker inspect --format "{{ index .Config.Labels \"com.docker.compose.project\"}}" $HOSTNAME)
links=($(docker inspect --format "{{range .NetworkSettings.Networks.${COMPOSE_PROJECT}_default.Links }}{{.}} {{end}}" $HOSTNAME))
links=(${links[@]%%:${TEMBOARD_HOSTNAME}})
PGCONTAINER=${links[@]%%*:*}
COMPOSE_SERVICE=$(docker inspect --format "{{ index .Config.Labels \"com.docker.compose.service\"}}" $HOSTNAME)

echo "Managing PostgreSQL container $PGCONTAINER." >&2

echo "Generating temboard-agent.conf" >&2

cat > /etc/temboard-agent/temboard-agent.conf <<EOF
# Generated by $0

[temboard]
home = /var/lib/temboard
users = /etc/temboard-agent/users
address = 0.0.0.0
port = 2345
ssl_cert_file = ${TEMBOARD_SSL_CERT-/usr/local/share/temboard-agent/quickstart/temboard-agent_CHANGEME.pem}
ssl_key_file = ${TEMBOARD_SSL_KEY-/usr/local/share/temboard-agent/quickstart/temboard-agent_CHANGEME.key}

[logging]
method = stderr

[postgresql]
host = /var/run/postgresql/
port = ${PGPORT}
dbname = ${PGDATABASE}
user = ${PGUSER}
password = ${PGPASSWORD}
instance = ${PGINSTANCE-main}

[monitoring]
collector_url = ${TEMBOARD_UI_URL%/}/monitoring/collector
ssl_ca_cert_file = ${TEMBOARD_SSL_CA-/usr/local/share/temboard-agent/quickstart/temboard-agent_ca_certs_CHANGEME.pem}

[administration]
pg_ctl = docker %s ${PGCONTAINER}
EOF


touch /etc/temboard-agent/users
chmod 0600 /etc/temboard-agent/users
for entry in ${TEMBOARD_USERS_LIST-alice:alice bob:bob} ; do
    echo "Adding user ${entry%%:*}."
    sed -i /${entry%:*}/d /etc/temboard-agent/users
    temboard-agent-password $entry >> /etc/temboard-agent/users
done

wait-for-it ${PGHOST}:${PGPORT}

register() {
    set -x
    hostportpath=${TEMBOARD_UI_URL#*://}
    hostport=${hostportpath%%/*}
    wait-for-it localhost:2345 -t 60
    wait-for-it ${hostport} -t 60

    temboard-agent-register \
        --host ${TEMBOARD_REGISTER_HOST-$COMPOSE_SERVICE} \
        --port ${TEMBOARD_REGISTER_PORT-2345} \
        --groups ${TEMBOARD_GROUPS-local_instances} \
        ${TEMBOARD_UI_URL%/}
}

if [ -z "${command##temboard-agent*}" -a -n "${TEMBOARD_UI_USER}" ] ; then
    register &
fi

set -x
exec ${command}

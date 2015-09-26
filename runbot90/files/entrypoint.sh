#!/bin/bash

set -e

# set odoo database host, port, user and password
: ${PGHOST:=$DBRUNBOT_PORT_5432_TCP_ADDR}
: ${PGPORT:=$DBRUNBOT_PORT_5432_TCP_PORT}
: ${PGUSER:=${DBRUNBOT_ENV_POSTGRES_USER:='postgres'}}
: ${PGPASSWORD:=$DBRUNBOT_ENV_POSTGRES_PASSWORD}

export PGHOST PGPORT PGUSER PGPASSWORD

${HOME}/instance/odoo/odoo.py

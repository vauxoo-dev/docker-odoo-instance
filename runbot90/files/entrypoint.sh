#!/bin/bash

set -e

source ${HOME}/.db_source
${HOME}/instance/odoo/odoo.py -c ${HOME}/instance/config/odoo_runbot.conf $1

#!/bin/bash

set -e

chown -R runbot:runbot ${EXTRA_ADDONS}/odoo-extra/runbot/static
chown -R runbot:runbot /home/runbot/.local/share/Odoo/filestore
chown -R runbot:runbot /var/log/supervisor
find /home/runbot/instance/extra_addons/odoo-extra/runbot -name res_config_view.xml -exec sed -i 's/base.menu_config/base.menu_administration/g' {} \;
source /home/runbot/.db_source

/usr/bin/supervisord

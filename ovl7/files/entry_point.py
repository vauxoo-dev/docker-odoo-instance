#!/usr/bin/python
# -*- coding: utf-8 -*-

from os import stat, path, getenv
from subprocess import call
from shutil import copy2
import pwd
import fileinput

filestore_path = '/home/odoo/instance/odoo/openerp/filestore'
configfile_path = '/home/odoo/instance/config/odoo.conf'

st = stat(filestore_path)
owner = pwd.getpwuid(st.st_uid).pw_name
if owner != "odoo":
    call(["chown", "-R", "odoo", filestore_path])

if not path.isfile(configfile_path):
    copy2("/external_files/odoo.conf", configfile_path)

if getenv('DB_SERVER'):
    for line in fileinput.input(configfile_path, inplace=True):
        if line.startswith('db_host'):
            print('db_host = %s' % getenv('DB_SERVER'))
        else:
            print(line.replace('\n', ''))

if getenv('DB_PORT'):
    for line in fileinput.input(configfile_path, inplace=True):
        if line.startswith('db_port'):
            print('db_port = %s' % getenv('DB_PORT'))
        else:
            print(line.replace('\n', ''))

st = stat(configfile_path)
owner = pwd.getpwuid(st.st_uid).pw_name
if owner != "odoo":
    call(["chown", "-R", "odoo", configfile_path])

call(["/usr/bin/supervisord"])

'''
Running locally. For Development.
'''

import subprocess

from cfg import SITE_WS, GIS_BASE, USER, DAMONS

subprocess.run('sudo chown -R {} {}/dist_site/*'.format(USER, SITE_WS), shell=True)
subprocess.run('sudo chown -R {} {}/dist_site'.format(USER, SITE_WS), shell=True)
subprocess.run('sudo chown -R {} {}/*'.format(USER, GIS_BASE), shell=True)
subprocess.run('cd {} && python3 gisliter.py'.format(SITE_WS), shell=True)
subprocess.run('sudo chown -R www-data.www-data {}/dist_site'.format(SITE_WS), shell=True)
subprocess.run('sudo chown -R www-data.www-data {}'.format(GIS_BASE), shell=True)

for dam in DAMONS:
    subprocess.run('sudo supervisorctl restart {}'.format(dam), shell=True)

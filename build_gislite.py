# -*- coding: utf-8 -*-
"""
发布程序入口
"""
import os
import shutil
import time

from gislite import gen_xlsx_lyr
from gislite import gen_mapproxy
from gislite import build_site
from config import TILE_SVR

STR_RUN_WCS_TMPL = '''#!/bin/bash
# mapproxy-util create -t base-config wcs_imgmap
# /usr/lib/python3-mapproxy/mapproxy-util serve-develop ./mapproxy.yaml -b 0.0.0.0:{port}
# ~/.local/bin/mapproxy-util serve-develop ./mapproxy.yaml -b 0.0.0.0:{port}
# mapproxy-util serve-develop ./mapproxy.yaml -b 0.0.0.0:{port}
/usr/lib/python3-mapproxy/mapproxy-util serve-develop ./mapproxy.yaml -b 0.0.0.0:{port}
'''

mapserver_ip = '127.0.0.1'
out_yaml_file = 'out_mapproxy.yaml'

start_time = time.time()

###########################################################

print('Generating mapfiles ...')
# gen_xlsx_lyr.run_it()
print('Generating mapproxy yaml ...')
# gen_mapproxy.gen_yaml_file(mapserver_ip, out_yaml_file)
print('build webgis ...')
build_site.run_it()

###########################################################
wcs_cache_dir = 'wcs_imgmap/cache_data'
if os.path.exists(wcs_cache_dir):
    shutil.rmtree(wcs_cache_dir)
else:
    os.makedirs(wcs_cache_dir)
shutil.move(out_yaml_file, './wcs_imgmap/mapproxy.yaml')


def gen_run_mapproxy_sh():
    ###########################################################
    # 生成运行 MapProxy 的脚本
    STR_RUN_WCS = STR_RUN_WCS_TMPL.format(port=TILE_SVR.split(':')[-1])
    with open('./wcs_imgmap/run_mapproxy.sh', 'w') as fo:
        fo.write(STR_RUN_WCS)


gen_run_mapproxy_sh()

end_time = time.time()

# 保存时间戳到文件。此文件用来判断要新处理的XLSX文件。
with open('mts.log', 'w') as fo:
    fo.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end_time)))

print('Running time: ', end_time - start_time)

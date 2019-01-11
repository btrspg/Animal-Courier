#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @License : Copyright(c) 2018 MIT License
# @Time    : 2019-01-09 15:01
# @Author  : YUELONG.CHEN
# @Mail    : yuelong_chen@yahoo.com
# @File    : psopen.py
# @Software: PyCharm

from __future__ import absolute_import, unicode_literals

import logging
import os
import subprocess
import sys
import time

import pandas as pd
import psutil

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))


def pspopen(cmd, prefix, interval=10):
    from animalcourier.formats import number
    from animalcourier.utils import file
    log = logging.getLogger('MRS')
    start = time.time()
    file.check_outfiles(prefix)
    with open(prefix + '.sh', 'w') as cmdout:
        cmdout.write('#! /bin/sh\n' + cmd + '\n')
    with psutil.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True) as p:
        log.info('now workon {}:{}...'.format(p.pid, os.path.basename(prefix)))
        with open(prefix + '.{}.o'.format(p.pid), 'w') as stdout:
            create_time = p.create_time()
            cache = {}
            local_time = 0
            while p.poll() is None and psutil.pid_exists(p.pid):
                children = p.children(recursive=True)
                for child in children:
                    cache = process_info(child, local_time, cache, os.path.basename(prefix))
                # stdout.write(str(p.memory_info()))
                # stdout.write('\n')
                # print(p.stdout.read().decode('utf8'))
                # stdout.write(p.stdout.read().decode('utf8'))
                local_time += interval
                time.sleep(interval)

            if p.poll() == 0:
                stdout.write(p.stdout.read().decode('utf8'))
                df = pd.DataFrame(cache)
                df[os.path.basename(prefix) + '.SUM'] = df.sum(axis=1)
                df.to_csv(prefix + '.' + str(p.pid) + '.csv')
                from animalcourier.plots.p_in_plotly import ploty_memorys
                ploty_memorys(df, os.path.basename(prefix), '{}.{}.html'.format(prefix, p.pid))
                with open(prefix + '.{}.e'.format(p.pid), 'w') as stderr:
                    stderr.write(p.stderr.read().decode('utf8'))
    # stdout, stderr = p.communicate()
    interval = (time.time() - start) / 60
    # write_out.write_out_err_cmd(cmd, pid, stdout, stderr, interval, prefix)
    log.info('finished {}:{}...'.format(p.pid, os.path.basename(prefix)))

    return number.float_normalized(interval), os.path.basename(prefix), prefix + '.' + str(p.pid) + '.csv'


def process_info(Process, stat_time, cache, name='work', ):
    '''

    :param Process: psutil.Process
    :param stat_time:
    :param cache:
    :param name:
    :return:
    '''
    name = '{cmd}-{pid}'.format(name=name, pid=Process.pid, cmd=Process.name())
    cache.setdefault(name, {})
    cache[name][stat_time] = Process.memory_info().rss
    return cache


def main():
    log_format = '%(asctime)s %(filename)s [%(levelname)s] %(message)s'
    logging.basicConfig(format=log_format, level=logging.INFO)
    log = logging.getLogger('MRS')
    # result = pspopen('for j in `seq 1 2`;do for i in `ls -R /home/chenyuelong/tmp/sentieon_AS3024/*`;do md5sum $i;done;done',
    #                  '/home/chenyuelong/tmp/test')
    result = pspopen('perl /home/chenyuelong/tmp/test2.pl', '/home/chenyuelong/tmp/test', 1)
    print(result)


if __name__ == '__main__':
    main()

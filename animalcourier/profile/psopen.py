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
import sys
import time

import pandas as pd
import psutil

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))


def pspopen(cmd, prefix, interval=10):
    from animalcourier.formats import number
    from animalcourier.utils import file
    # from animalcourier.utils.shell_cmd import shell_header
    log = logging.getLogger('MRS')
    start = time.time()
    file.check_outfiles(prefix)
    # with open(prefix + '.sh', 'w') as cmdout:
    #     cmdout.write(shell_header + cmd + '\n')
    stdout = '{prefix}.o'.format(prefix=prefix)
    stderr = '{prefix}.e'.format(prefix=prefix)
    with psutil.Popen(cmd, stderr=open(stderr, 'w'), stdout=open(stdout, 'w'), shell=True) as p:
        log.info('now workon {work}:pid({pid}) ...'.format(pid=p.pid, work=os.path.basename(prefix)))

        create_time = p.create_time()
        cache = {}
        local_time = 0
        while p.poll() is None and psutil.pid_exists(p.pid):
            children = p.children(recursive=True)
            for child in children:
                cache = process_info(child, local_time, cache, os.path.basename(prefix))
            local_time += interval
            time.sleep(interval)

        if p.poll() == 0:
            df = pd.DataFrame(cache)
            df[os.path.basename(prefix) + '.SUM'] = df.sum(axis=1)
            df.to_csv(prefix + '.' + str(p.pid) + '.csv')
            from animalcourier.plots.p_in_plotly import ploty_memorys
            ploty_memorys(df, os.path.basename(prefix), '{}.{}.html'.format(prefix, p.pid))

    interval = (time.time() - start) / 60
    log.info('finished {work}:pid({pid}) ...'.format(pid=p.pid, work=os.path.basename(prefix)))

    return number.float_normalized(interval), os.path.basename(prefix), prefix + '.' + str(p.pid) + '.csv'


def process_info(Process, stat_time, cache, name='work', ):
    '''

    :param Process: psutil.Process
    :param stat_time:
    :param cache:
    :param name:
    :return:
    '''
    try:
        name = '{cmd}-{pid}'.format(name=name, pid=Process.pid, cmd=Process.name())
        cache.setdefault(name, {})
        cache[name][stat_time] = Process.memory_info().rss
    except Exception:
        name = 'tmp'
        cache.setdefault(name,{})
        cache[name][stat_time] = 0
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

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @License : Copyright(c) 2018 MIT License
# @Time    : 2018-12-27 21:54
# @Author  : YUELONG.CHEN
# @Mail    : yuelong_chen@yahoo.com
# @File    : multi_run.py
# @Software: PyCharm

from __future__ import absolute_import, unicode_literals

import argparse
import logging
import os
import subprocess
import time
from multiprocessing import Pool

import pandas as pd

log_format = '%(asctime)s %(filename)s [%(levelname)s] %(message)s'
# logging.basicConfig(format=log_format, level=logging.INFO)
log = logging.getLogger('MRS')
log_stdout = logging.StreamHandler()
log_stdout.setFormatter(logging.Formatter(log_format))
log_stdout.setLevel(logging.INFO)
log.addHandler(log_stdout)


# TODO:Move methods in to another Tree
# TODO:modify logs
# TODO:add another args for log dir
def get_args():
    parser = argparse.ArgumentParser(description='For shell scripts run',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--shell', required=True, action='store',
                        help='shell scripts')
    parser.add_argument('--thread', default=4, type=int, action='store',
                        help='thread number')
    parser.add_argument('--work-name', default='work', type=str,
                        help='logs name prefix')
    return parser.parse_args()


# TODO:Move methods in to another Tree
# TODO: add a count, like 24 tasks this is number 10 [10/24]
def popen(cmd, prefix):
    from animalcourier.formats import number
    p = subprocess.Popen(cmd, stderr=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         shell=True)
    pid = p.pid
    start = time.time()
    log.info('Start to run the cmd in {}:{}...'.format(pid, os.path.basename(prefix)))
    stdout, stderr = p.communicate()
    interval = (time.time() - start) / 60
    write_out_err_cmd(cmd, pid, stdout, stderr, interval, prefix)
    log.info('Finshed the cmd in {}:{}...'.format(pid, os.path.basename(prefix)))

    return number.float_normalized(interval), os.path.basename(prefix)


def write_out_err_cmd(cmd, pid, out, err, cost_time, prefix):
    '''

    :param cmd:
    :param pid:
    :param out:
    :param err:
    :param cost_time:
    :param prefix:
    :return:
    '''

    prefix = '{prefix}.{pid}'.format(prefix=prefix, pid=pid)
    log.info('Write both stdout and stderr log in {} [prefix]'.format(prefix))
    with open(prefix + '.o', 'w') as obuf, open(prefix + '.e', 'w') as ebuf, open(prefix + '.sh', 'w') as cmdbuf:
        cmdbuf.write('#! /bin/sh\n{}'.format(cmd))
        obuf.write('COST:{}\n\n\nCMD:{}\n\n\n'.format(cost_time, cmd))
        obuf.write(out.decode('utf8'))
        ebuf.write(err.decode('utf8'))


# TODO:Move methods in to another Tree
def get_cmds(shell_script, work_log, work_name):
    from animalcourier.formats import number
    cmds = []
    n = 0
    with open(shell_script, 'r') as f:
        line = f.readline()

        while line:
            # print(line)
            line = line.strip('\n')
            if (not line.startswith('#')) and line != '':
                n += 1
                prefix = '{work_log}/{work_name}{number}/'.format(work_log=work_log,
                                                                  work_name=work_name,
                                                                  number=number.normalized(n, 4))
                os.makedirs(prefix, 0o755, exist_ok=True)

                cmds.append([line, '{prefix}/{work_name}{number}'.format(prefix=prefix,
                                                                         work_name=work_name,
                                                                         number=number.normalized(n, 4))])
            line = f.readline()
    return cmds


def main():
    args = get_args()
    work_log = './log.{work}.{date}'.format(
        work=args.work_name,
        date=time.strftime("%Y%m%d%H%M%S", time.localtime())
    )
    log_file = logging.FileHandler('{work_log}.log'.format(work_log=work_log))
    log_file.setFormatter(logging.Formatter(log_format))
    log_file.setLevel(logging.INFO)
    log.addHandler(log_file)

    os.makedirs(work_log)
    log.info('Get command args, and args are :{}'.format(args.shell))
    pool = Pool(args.thread)
    cmds = get_cmds(args.shell, work_log, args.work_name)

    all_infos = pool.starmap(popen, cmds)
    pool.close()
    pool.join()
    log.info('ALL FINISHED!!')
    # log.info('===' * 30)
    summary = pd.DataFrame(all_infos, columns=['Time(mins)', 'Work'])
    print('==' * 30)
    print(summary.to_string())
    print('==' * 30)
    print(summary['Time(mins)'].astype(float).describe())


if __name__ == '__main__':
    main()

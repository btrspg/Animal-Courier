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

logging.basicConfig(format='%(asctime)s %(filename)s [%(levelname)s] %(message)s', level=logging.INFO)
log = logging.getLogger('MRS')


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
    return parser.parse_args()


# TODO:Move methods in to another Tree
# TODO: add a count, like 24 tasks this is number 10 [10/24]
def popen(cmd):
    p = subprocess.Popen(cmd, stderr=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         shell=True)
    pid = p.pid
    start = time.time()
    log.info('Start to run the cmd in {}:{}...'.format(pid, cmd[0:10]))
    stdout, stderr = p.communicate()
    write_out_err(cmd, pid, stdout, stderr)
    interval = (time.time() - start) / 60
    log.info('Finshed the cmd in {}:{}...'.format(pid, cmd[0:10]))

    return interval


def write_out_err(cmd, pid, out, err):
    '''

    :param cmd:
    :param pid:
    :param out:
    :param err:
    :return:
    '''

    tag = cmd.replace('/', '_').split(' ')[0]
    prefix = './log/{tag}.{pid}'.format(tag=tag, pid=pid)
    log.info('Write both stdout and stderr log in {} [prefix]'.format(prefix))
    with open(prefix + '.o', 'w') as obuf, open(prefix + '.e', 'w') as ebuf:
        obuf.write('CMD:{}\n\n\n'.format(cmd))
        obuf.write(out.decode('utf8'))
        ebuf.write(err.decode('utf8'))


# TODO:Move methods in to another Tree
def get_cmds(shell_script):
    cmds = []
    with open(shell_script, 'r') as f:
        line = f.readline()

        while line:
            # print(line)
            line = line.strip('\n')
            if (not line.startswith('#')) and line != '':
                cmds.append(line)
            line = f.readline()
    return cmds


def main():
    args = get_args()
    os.makedirs('./log')
    log.info('Get command args, and args are :{}'.format(args.shell))
    pool = Pool(args.thread)
    cmds = get_cmds(args.shell)

    result = pool.map(popen, cmds)
    pool.close()
    pool.join()
    for i, j in zip(cmds, result):
        print('COST %.2f mins! , CMD: %s ,' % (j, i))


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @License : Copyright(c) 2018 MIT License
# @Time    : 2019-01-11 10:32
# @Author  : YUELONG.CHEN
# @Mail    : yuelong_chen@yahoo.com
# @File    : shell_cmd.py
# @Software: PyCharm

from __future__ import absolute_import, unicode_literals

import logging
import os
import subprocess
import sys
import time

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))


# TODO: add a count, like 24 tasks this is number 10 [10/24]
def popen(cmd, prefix, interval=''):
    from animalcourier.formats import number
    # from .write_out import write_out_err_cmd
    log = logging.getLogger('MRS')
    stdout = '{prefix}.o'.format(prefix=prefix)
    stderr = '{prefix}.e'.format(prefix=prefix)
    p = subprocess.Popen(cmd, stderr=open(stderr, 'w'),
                         stdout=open(stdout, 'w'),
                         shell=True)
    pid = p.pid
    start = time.time()
    log.info('now workon {work}:pid({pid}) ...'.format(pid=pid, work=os.path.basename(prefix)))
    _, stderr = p.communicate()
    interval = (time.time() - start) / 60
    # write_out_err_cmd(cmd, pid, stdout, stderr, interval, prefix)
    log.info('finished {work}:pid({pid}) ...'.format(pid=pid, work=os.path.basename(prefix)))

    return number.float_normalized(interval), os.path.basename(prefix), ''


def cmd2shell(cmd, file):
    '''

    :param cmd:
    :param file:
    :return:
    '''
    shell_header = '''#!/bin/bash
set -e
set -o pipefail
trap '' USR1 USR2 XCPU
echo "This task is running as pid $$ on ${HOSTNAME}" >&2
echo "CWD is `pwd`" >&2


    '''
    with open(file, 'w') as f:
        f.write(shell_header + '\n')
        f.write(cmd + '\n')
    os.chmod(file, 0o755)
    return file


def get_cmds(shell_script, work_log, work_name, interval):
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
                prefix = '{work_log}/{work_name}.{number}/'.format(work_log=work_log,
                                                                   work_name=work_name,
                                                                   number=number.normalized(n, 4))
                os.makedirs(prefix, 0o755, exist_ok=True)

                cmds.append([cmd2shell(line, '{prefix}/{work_name}.{number}.sh'.format(prefix=prefix,
                                                                                       work_name=work_name,
                                                                                       number=number.normalized(n, 4))),
                             '{prefix}/{work_name}.{number}'.format(prefix=prefix,
                                                                    work_name=work_name,
                                                                    number=number.normalized(n, 4)), interval])
            line = f.readline()
    return cmds


def main():
    import tempfile
    tmp = tempfile.gettempdir()
    for i in get_cmds('../..//tests/test.sh', tmp, 'test', 10):
        print(i)


if __name__ == '__main__':
    main()

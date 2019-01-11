#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @License : Copyright(c) 2018 MIT License
# @Time    : 2019-01-07 10:51
# @Author  : YUELONG.CHEN
# @Mail    : yuelong_chen@yahoo.com
# @File    : write_out.py
# @Software: PyCharm

from __future__ import absolute_import, unicode_literals

import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))


def write_both_file_and_stream(content, file):
    '''
    主要为了输出log一类的文件，需要保存一个log文件，并且在标准输出中打印出来
    :param content:
    :param file:
    :return:
    '''
    with open(file, 'a') as f:
        f.write(content + '\n')
        print(content)


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
    import logging
    log = logging.getLogger('MRS')
    prefix = '{prefix}.{pid}'.format(prefix=prefix, pid=pid)
    log.info('Write both stdout and stderr log in {} [prefix]'.format(prefix))
    with open(prefix + '.o', 'w') as obuf, open(prefix + '.e', 'w') as ebuf, open(prefix + '.sh', 'w') as cmdbuf:
        cmdbuf.write('#! /bin/sh\n{}\n'.format(cmd))
        obuf.write('COST:{}\n\n\nCMD:{}\n\n\n'.format(cost_time, cmd))
        obuf.write(out.decode('utf8'))
        ebuf.write(err.decode('utf8'))


def main():
    pass


if __name__ == '__main__':
    main()

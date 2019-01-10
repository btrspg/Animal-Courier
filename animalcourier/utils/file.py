#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @License : Copyright(c) 2018 MIT License
# @Time    : 2019-01-09 16:43
# @Author  : YUELONG.CHEN
# @Mail    : yuelong_chen@yahoo.com
# @File    : file.py
# @Software: PyCharm

from __future__ import absolute_import, unicode_literals

import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

__doc__ = '''
一般文件的操作，包括目录
'''


def check_outfiles(*files):
    '''

    :param files:
    :return:
    '''
    try:
        [os.makedirs(os.path.dirname(file), exist_ok=True) for file in files]
    except PermissionError as e:
        raise PermissionError(e.args)
    return True


def check_output_dirs(*dirs):
    '''

    :param dirs:
    :return:
    '''
    try:
        [os.makedirs(sdir, exist_ok=True) for sdir in dirs]
    except PermissionError as e:
        raise PermissionError(e.args)
    return True

def check_infiles(*files):
    '''

    :param files:
    :return:
    '''

    exists = [os.path.exists(file) for file in files]
    if all(exists):
        return True
    else:
        raise FileNotFoundError('[{}] not found.'.format(files[exists.index(False)]))


def main():
    print(check_infiles('write_out.py', 'gogo'))


if __name__ == '__main__':
    main()

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

    :param content:
    :param file:
    :return:
    '''
    with open(file, 'a') as f:
        f.write(content+'\n')
        print(content)


def main():
    pass


if __name__ == '__main__':
    main()

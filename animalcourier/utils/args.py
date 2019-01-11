#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @License : Copyright(c) 2018 MIT License
# @Time    : 2019-01-11 10:31
# @Author  : YUELONG.CHEN
# @Mail    : yuelong_chen@yahoo.com
# @File    : args.py
# @Software: PyCharm

from __future__ import absolute_import, unicode_literals

import argparse
import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))


def get_args():
    parser = argparse.ArgumentParser(description='For shell scripts run',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--shell', required=True, action='store',
                        help='shell scripts')
    parser.add_argument('--thread', default=4, type=int, action='store',
                        help='thread number')
    parser.add_argument('--work-name', default='work', type=str,
                        help='logs name prefix')
    parser.add_argument('--profile', action='store_true',
                        help='If run profile for command(only RSS)')
    parser.add_argument('--interval', type=int, default=10,
                        help='If profile set True, please set interval(seconds) of the memory stats')
    return parser.parse_args()


def main():
    pass


if __name__ == '__main__':
    main()

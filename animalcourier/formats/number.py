#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @License : Copyright(c) 2018 MIT License
# @Time    : 2019-01-04 10:27
# @Author  : YUELONG.CHEN
# @Mail    : yuelong_chen@yahoo.com
# @File    : number.py
# @Software: PyCharm

from __future__ import absolute_import, unicode_literals

import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))


def normalized(number, length=4):
    '''
    change 1 -> 00001 if number=1,length=5
    change 12345 -> 12345 if number=12345, length=4 (length < real length)
    :param number:
    :param length:
    :return:
    '''
    if len(str(number)) > length:
        return str(number)
    else:
        return '0' * (length - (len(str(number)))) + str(number)


def float_normalized(number, length=2):
    '''
    change 1.2343234-> 1.24 if number=1.2343234,length=2
    :param number:
    :param length:
    :return:
    '''
    norm = '%.{}f'.format(length)
    return norm % number


def main():
    print(normalized(32))
    print(normalized(22234, 4))
    print(normalized(43, 7))
    print(float_normalized(1.222))
    print(float_normalized(42))
    print(float_normalized(1.33, 4))


if __name__ == '__main__':
    main()

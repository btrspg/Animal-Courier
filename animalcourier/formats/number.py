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
    :param number:
    :param length:
    :return:
    '''
    if len(str(number)) > length:
        return str(number)
    else:
        return '0' * (length - (len(str(number)))) + str(number)


def main():
    print(normalized(32))
    print(normalized(22234, 4))
    print(normalized(43, 7))


if __name__ == '__main__':
    main()

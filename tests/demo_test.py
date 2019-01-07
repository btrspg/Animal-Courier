#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @License : Copyright(c) 2018 MIT License
# @Time    : 2018-12-27 22:54
# @Author  : YUELONG.CHEN
# @Mail    : yuelong_chen@yahoo.com
# @File    : demo_test.py
# @Software: PyCharm

from __future__ import absolute_import, unicode_literals

import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))


class TestStringMethods(unittest.TestCase):

    def test_format(self):
        from animalcourier.formats import number
        self.assertEqual('00232', number.normalized(232, 5))
        self.assertEqual('444', number.normalized(444, 2))
        self.assertEqual('1.22', number.float_normalized(1.2244))
        self.assertEqual('0.4', number.float_normalized(0.4444444, length=1))

    # def test_utils(self):
    #     from animalcourier.utils import write_out
    #     write_out.write_both_file_and_stream('test', 'testfile')
    #     self.assertFalse(not os.path.exists('testfile'))


if __name__ == '__main__':
    unittest.main()

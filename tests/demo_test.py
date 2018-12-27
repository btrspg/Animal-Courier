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

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()

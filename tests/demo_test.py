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
import tempfile
import unittest

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))


class TestStringMethods(unittest.TestCase):

    def test_format(self):
        from animalcourier.formats import number
        self.assertEqual('00232', number.normalized(232, 5))
        self.assertEqual('444', number.normalized(444, 2))
        self.assertEqual('1.22', number.float_normalized(1.2244))
        self.assertEqual('0.4', number.float_normalized(0.4444444, length=1))
        self.assertEqual('1.23T', number.big_number_normalized(1230000000000))

    def test_utils(self):
        from animalcourier.utils import write_out, file
        write_out.write_both_file_and_stream('test', 'testfile')
        self.assertFalse(not os.path.exists('testfile'))
        self.assertFalse(not file.check_infiles(__file__))
        # self.assertRaises(file.check_infiles(__file__ + 'test'), FileNotFoundError)
        tmp = tempfile.gettempdir()
        file.check_outfiles(*['{0}/test{1}/test{1}'.format(tmp, number) for number in range(10)])
        self.assertFalse(not file.check_infiles(
            *[os.path.dirname('{0}/test{1}/test{1}'.format(tmp, number)) for number in range(10)]))
        # self.assertRaises(file.check_outfiles('/test/test1'), PermissionError)
        # self.assertRaises(file.check_outfiles('/test/'), PermissionError)


if __name__ == '__main__':
    unittest.main()

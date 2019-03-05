#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @License : Copyright(c) MIT Lisence
# @Time    : 2019-03-05 13:14
# @Author  : YUELONG.CHEN
# @Mail    : yuelong_chen@yahoo.com
# @File    : notify.py
# @Software: PyCharm

from __future__ import absolute_import, unicode_literals


def add_pushbullet(apobj, token):
    '''

    :param apobj:
    :param token:
    :param title:
    :param context:
    :return:
    '''
    apobj.add('pbul://{token}'.format(token=token))
    return apobj


def send_sns(apobj, title, context):
    '''

    :param apobj:
    :param title:
    :param context:
    :return:
    '''
    apobj.notify(
        body=context,
        title=title,
    )


def new_notify():
    import apprise
    return apprise.Apprise()


def main():
    import apprise

    apobj = apprise.Apprise()
    apobj = add_pushbullet(apobj, 'o.F5T9F0z54yJNQixDpQYtwqO7x3NJzUrC')
    send_sns(apobj, title='test', context='test2')


if __name__ == '__main__':
    main()

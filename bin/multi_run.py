#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @License : Copyright(c) 2018 MIT License
# @Time    : 2018-12-27 21:54
# @Author  : YUELONG.CHEN
# @Mail    : yuelong_chen@yahoo.com
# @File    : multi_run.py
# @Software: PyCharm

from __future__ import absolute_import, unicode_literals

import logging
import os
import time
from multiprocessing import Pool

import pandas as pd


def main():
    from animalcourier.utils import write_out, shell_cmd, args
    import platform
    log_format = '%(asctime)s %(filename)s [%(levelname)s] %(message)s'
    logging.basicConfig(format=log_format, level=logging.INFO)
    log = logging.getLogger('MRS')
    token = None
    title = ''
    context = ''
    args = args.get_args()
    if args.notification:
        token = os.getenv('pushBullet_token', None)
        if None is token:
            raise ValueError('You should export pushBullet_token if you need Notification!!')
        user = os.getenv('USER')
        pwd = os.getenv('PWD')
        node = platform.node()
        project = args.work_name
        title = '{user}:{project} finished!'.format(user=user, project=project)
        context = 'NODE:{node}\nPWD:{pwd}\n'.format(node=node, pwd=pwd)

    work_log = './log.{work}.{date}'.format(
        work=args.work_name,
        date=time.strftime("%Y%m%d%H%M%S", time.localtime())
    )
    log_file = logging.FileHandler('{work_log}.log'.format(work_log=work_log))
    log_file.setFormatter(logging.Formatter(log_format))
    log_file.setLevel(logging.INFO)
    log.addHandler(log_file)

    os.makedirs(work_log)
    log.info('Get command args, and args are :{}'.format(args.shell))
    pool = Pool(args.thread)
    cmds = shell_cmd.get_cmds(args.shell, work_log, args.work_name, args.interval)
    # print(cmds)
    # for i in cmds:
    #     print(i)
    if args.profile:
        from animalcourier.profile.psopen import pspopen
        all_infos = pool.starmap(pspopen, cmds)
    else:
        all_infos = pool.starmap(shell_cmd.popen, cmds)
    pool.close()
    pool.join()

    # log.info('===' * 30)
    log.info('Stats time of work')
    summary = pd.DataFrame(all_infos, columns=['Time(mins)', 'Work', 'Profile'])
    if args.profile:
        log.info('Stats profiles')
        merge_data = ''
        for _, _, csv in all_infos:
            # print('csv:\t'+csv)
            if not os.path.exists(csv): continue
            data = pd.read_csv(csv, index_col=0)
            merge_data = data[data.columns[-1]].to_frame() if isinstance(merge_data, str) else merge_data.join(
                data[data.columns[-1]], how='outer')
        from animalcourier.plots import p_in_plotly
        if isinstance(merge_data, str):
            print('No plots due to no files')
        else:
            p_in_plotly.ploty_memorys(merge_data, title=os.path.basename(work_log), filename=work_log + '.html')
    describe = summary['Time(mins)'].astype(float).describe().to_string()
    if args.notification:
        from animalcourier.utils import notify
        ntf = notify.new_notify()
        if None is not token:
            ntf = notify.add_pushbullet(ntf, token)
            notify.send_sns(ntf, title, context + "\n"
                            + summary.to_string() +
                            "\n" + describe)

    log.info('ALL FINISHED!!')
    write_out.write_both_file_and_stream('==' * 30, '{work_log}.log'.format(work_log=work_log))
    write_out.write_both_file_and_stream(summary.to_string(), '{work_log}.log'.format(work_log=work_log))
    write_out.write_both_file_and_stream('==' * 30, '{work_log}.log'.format(work_log=work_log))

    # print(describe)
    write_out.write_both_file_and_stream(describe, '{work_log}.log'.format(work_log=work_log))


if __name__ == '__main__':
    main()

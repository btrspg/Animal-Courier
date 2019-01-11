#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @License : Copyright(c) 2018 MIT License
# @Time    : 2019-01-10 23:14
# @Author  : YUELONG.CHEN
# @Mail    : yuelong_chen@yahoo.com
# @File    : plotly.py
# @Software: PyCharm

from __future__ import absolute_import, unicode_literals

import os
import sys

import plotly
import plotly.graph_objs as go

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))


def main():
    file = '/home/chenyuelong/tmp/test.15748.csv'
    import pandas as pd
    data = pd.read_csv(file, index_col=0)
    data['Sun'] = data.sum(axis=1)
    ploty_lines(data, title='test', filename='/home/chenyuelong/tmp/plot_test.html')


def ploty_lines(dataframe, title='line-plots', filename='temp-plot.html'):
    '''

    :param dataframe:
    :param title:
    :param filename:
    :return:
    '''
    plot_dict = {}
    plot_dict = _resolve_dataframe(dataframe, plot_dict)
    plot_dict['layout'] = {
        'title': title,
        'xaxis': dict(
            title='Time(seconds)',
            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
        ),
        'yaxis': dict(
            title='Resident Set Size(bytes)',
            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
        )

    }
    plotly.offline.plot(plot_dict, show_link=True, link_text='Export to plot.ly', validate=True,
                        output_type='file', include_plotlyjs=True, filename=filename, auto_open=False,
                        image=None, image_filename=filename, image_width=800, image_height=600, config=None,
                        include_mathjax=False)


def _resolve_dataframe(dataframe, cache=None):
    '''

    :param dataframe:
    :param cache:
    :return:
    '''
    if None is cache:
        cache = {}

    cache.setdefault('data', [])
    # print(cache)
    for col in dataframe.columns:
        cache['data'].append(go.Scatter(x=dataframe.index, y=dataframe[col], name=col, fill='tozeroy'))
    return cache


if __name__ == '__main__':
    main()

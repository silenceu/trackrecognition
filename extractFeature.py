#! /usr/bin/python3
# -*- encoding: utf-8 -*-
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import pylab as pl


def readdata(filepath):
    """
    读取文件,返回轨迹数据,返回类型为pandas的Series,包含3000个list,每个为n*3大小:[[x,y,t],[x,y,t],...,[x,y,t]]
    """
    column_name = ['id', 'trace', 'target', 'label']
    df = pd.read_csv(filepath, sep=' ', header=None, names=column_name)
    traces = df.loc[:, 'trace']
    traces = traces.apply(lambda trace: [point.split(',') for point in trace.split(';')[:-1]])
    return traces

def extract_avg_speed(trace: list):
    """
    提取平均速度,参数为一个list,大小是n*3:[[x,y,t],[x,y,t],...,[x,y,t]]
    """
    trace = np.array(trace, dtype='int32')
    trace = trace.T
    avg_speed = (trace[0].max() - trace[0].min()) / (trace[2].max() - trace[2].min())
    return avg_speed


# 增加提取新特征的方法
# 该函数只是针对一条规矩数据进行特征提取
# def extract_feature(trace: list):
#     trace = np.array(trace, dtype='int32')
#     trace = trace.T
#     # 处理过程
#     return feature
#
#
# 在main()添加以下形式的语句调用extract_feature方法处理所以轨迹数据获取3000个特征
# features = traces.apply(extrac_feature)
#

def main():
    traces = readdata('data_traing.txt')
    avg_speeds = traces.apply(extrac_avg_speed) # 使用extract_avg_speed提取平均速度
    print(avg_speeds)


if __name__ == '__main__':
    main()
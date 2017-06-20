#! /usr/bin/python3
# -*- encoding: utf-8 -*-
import numpy as np
import pandas as pd


def readdata(filepath):
    """
    读取文件,返回轨迹数据,返回类型为pandas的Series,包含3000个numpy类型二维数组,每个为n*3大小:[[x,y,t],[x,y,t],...,[x,y,t]]
    """
    column_name = ['id', 'trace', 'target', 'label']
    df = pd.read_csv(filepath, sep=' ', header=None, names=column_name)
    traces = df.loc[:, 'trace']
    traces = traces.apply(lambda trace: [point.split(',') for point in trace.split(';')[:-1]])
    traces = traces.apply(lambda trace: np.array(trace, dtype='int32'))
    return traces


def extract_avg_speed(trace: np.ndarray):
    """
    提取平均速度,参数为一个numpy二维数组,大小是n*3:[[x,y,t],[x,y,t],...,[x,y,t]]
    """
    trace = trace.T
    avg_speed = (trace[0].max() - trace[0].min()) / (trace[2].max() - trace[2].min())
    return avg_speed


def extract_size(trace: np.ndarray):
    """
    随便添加一个用来测试
    """
    return trace.size

# 增加提取新特征的方法
# 该函数只是针对一条轨迹数据进行特征提取
# def extract_feature(trace: np.ndarray):
#     # 处理过程
#     return feature
#
#
# 在main()添加以下形式的语句调用extract_feature方法处理所有轨迹数据获取3000个特征
# features = traces.apply(extract_feature)


def main():
    traces = readdata('data_training.txt')
    avg_speeds = traces.apply(extract_avg_speed)  # 使用extract_avg_speed提取平均速度
    print(avg_speeds)


if __name__ == '__main__':
    main()

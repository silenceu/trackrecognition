#! /usr/bin/python3
# -*- encoding: utf-8 -*-
import numpy as np
import pandas as pd
from extractFeature import readdata
from extractFeature import extract_avg_speed, extract_size
from pandas import DataFrame


def apply_all(functions: list, traces: pd.DataFrame):
    """
    所有提取特征的函数以列表的形式传入,提取所有的特征然后以numpy矩阵的形式返回
    """
    features = DataFrame(np.zeros((traces.size, len(functions))))
    for idx, extract_func in enumerate(functions):
        features[idx] = traces.apply(extract_func)
    return features.values


def main():
    traces = readdata('data_training.txt')
    funcs = [extract_avg_speed, extract_size]
    X = apply_all(funcs, traces)
    print(X.shape)
    print(X)

if __name__ == '__main__':
    main()

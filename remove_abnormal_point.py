from extractFeature import readdata
import numpy as np


def check(trace: np.ndarray):
    trace = trace[:-1]
    for idx in range(len(trace)-1):
        if trace[idx + 1][2] < trace[idx][2]:
            return False
    return True


def get_result_mark():
    """
    返回一个3000大小的bool数组,标记每条数据是否有时间乱序问题
    使用方法假设 x, labels 是3000训练集和标签
    marks = get_result_mark()
    x = x[marks]
    labels = labels[marks]
    :return:
    """
    traces, _ = readdata('data_train.txt')
    return traces.apply(check).values


def main():
    result = get_result_mark()
    print(result)

if __name__ == '__main__':
    main()

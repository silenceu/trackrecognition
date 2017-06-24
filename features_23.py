from extractFeature import get_feature_list, readdata, readtestdata
from generate_train_data import apply_all


functions = get_feature_list()


def get_train_data():
    """
    计算训练数据特征，返回特征矩阵和对应的类别标签
    """
    traces, labels = readdata('data_train.txt')
    x = apply_all(functions, traces)
    return x, labels


def get_test_data():
    """
    计算测试数据特征，返回特征矩阵
    """
    traces = readtestdata('data_test.txt')
    x = apply_all(functions, traces)
    return x

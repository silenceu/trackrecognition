from extractFeature import readdata
import numpy as np


def trace_sort(trace: np.ndarray):
    trace = trace[:-1]
    return sorted(trace, key=lambda x: x[2])


def get_sorted_trace():
    traces, _ = readdata('data_train.txt')
    sorted_traces = traces.apply(trace_sort)
    return sorted_traces


def main():
    traces, _ = readdata('data_train.txt')
    sorted_traces = traces.apply(trace_sort)
    print(sorted_traces[0])

if __name__ == '__main__':
    main()
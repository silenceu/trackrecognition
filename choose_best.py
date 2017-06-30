from itertools import combinations
from numpy import loadtxt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
from xgboost.sklearn import XGBClassifier
from xgboost.sklearn import XGBRegressor
from remove_abnormal_point import get_result_mark

marks = get_result_mark()
idx = list(range(6))
raw_x = loadtxt('train_feature630.txt', delimiter=' ')
labels = loadtxt('labels.txt', delimiter=' ')
raw_x = raw_x[marks]
labels = labels[marks]
# x_test = loadtxt('train_feature.txt', delimiter=' ')
seed = 10
test_size = 0.3

max_idx = list()
max_score = 0

for i in range(1, 7):
    sub_idxs = list(combinations(idx, i))
    for sub_idx in sub_idxs:
        # print(list(sub_idx), raw_x.shape)
        x = raw_x[:, list(sub_idx)]
        # print(len(x))
        x_train, x_test, y_train, y_test = train_test_split(x, labels, test_size=test_size, random_state=seed)
        # model = XGBClassifier(learning_rate=0.01,
        #                       # seed=seed,
        #                       max_depth=10,
        #                       silent=1)
        model = XGBRegressor(max_depth=10)
        model.fit(x_train, y_train)
        y_pre = model.predict(x_test)
        predictions = [round(value) for value in y_pre]
        accuracy = accuracy_score(y_test, predictions)
        if accuracy > max_score:
            max_score = accuracy
            max_idx = np.copy(sub_idx)

print(max_score, max_idx)

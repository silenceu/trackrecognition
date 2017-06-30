from xgboost.sklearn import XGBRegressor
import numpy as np
from remove_abnormal_point import get_result_mark

# load data
marks = get_result_mark()
X = np.loadtxt('train_feature630.txt', delimiter=' ')
y = np.loadtxt('labels.txt', delimiter=' ')
X = X[marks]
y = y[marks]
X_test = np.loadtxt('test_feature630.txt', delimiter=' ')
X = np.nan_to_num(X)
y = np.nan_to_num(y)
X = X[:, [0, 1, 3, 4, 5]]
X_test = np.nan_to_num(X_test)
X_test = X_test[:, [0, 1, 3, 4, 5]]

model = XGBRegressor(max_depth=10)
model.fit(X, y)

# make predictions for test data
y_pre = model.predict(X_test)

# get result
num = np.arange(1, 100001)
result = num[y_pre < 0.99]
np.savetxt('BDC0642_20170630.txt', result, '%d')
print(result.shape)

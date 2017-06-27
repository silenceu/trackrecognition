from xgboost import XGBClassifier
import numpy as np

# load data
X = np.loadtxt('train_feature.txt', delimiter=' ')
y = np.loadtxt('labels.txt', delimiter=' ')
X_test = np.loadtxt('test_feature.txt', delimiter=' ')
X = np.nan_to_num(X)
y = np.nan_to_num(y)
X = X[:, [0, 2, 3, 4]]
X_test = np.nan_to_num(X_test)
X_test = X_test[:, [0, 2, 3, 4]]

model = XGBClassifier(learning_rate=0.01)
model.fit(X, y)

# make predictions for test data
y_pre = model.predict(X_test)

# get result
num = np.arange(1, 100001)
result = num[y_pre == 0]
np.savetxt('BDC0642_20170627.txt', result, '%d')
print(result.shape)

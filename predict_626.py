from xgboost import XGBClassifier
import numpy as np

# load data
X = np.loadtxt('train_feature.txt', delimiter=' ')
y = np.loadtxt('labels.txt', delimiter=' ')
X_test = np.loadtxt('test_feature.txt', delimiter=' ')
X = np.nan_to_num(X)
y = np.nan_to_num(y)
X_test = np.nan_to_num(X_test)

model = XGBClassifier(learning_rate=0.01)
model.fit(X, y)

# make predictions for test data
y_pre = model.predict(X_test)

# get result
num = np.arange(1, 100001)
result = num[y_pre == 0]
np.savetxt('result_623_new_6.txt', result, '%d')
print(result.shape)

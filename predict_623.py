from xgboost import XGBClassifier
from features_23 import get_train_data, get_test_data
import numpy as np

# load data
X, y = get_train_data()
X_test = get_test_data()
X = np.nan_to_num(X)
y = np.nan_to_num(y)
X_test = np.nan_to_num(X_test)

model = XGBClassifier()
model.fit(X, y)

# make predictions for test data
y_pre = model.predict(X_test)

# get result
num = np.arange(1, 100001)
result = num[y_pre == 0]
np.savetxt('result_623.txt', result, '%d')
print(result.shape)

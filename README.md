# 鼠标轨迹识别 - 三个臭皮匠胜过诸葛亮

语言：python3

需要用到的模块：matplotlib、pandas、numpy

#### 模块功能:
- showTrace   轨迹可视化
- extractFeature   提取特征
- generate_train_data   合并计算所以特征集合
- features\_[date]   获取最终的训练数据和标签、预测数据
- predict_[date]  建模预测最终结果

###  提交日志

-   2017-06-24
    -   修改extractFeature,generate_train_data
    -   增加features\_[date], predict\_[date]模块
    -   新增加的features\_[date]模块调用extractFeature和generate_train_data获取最终的训练数据和标签、预测数据
    -   新增加的predict\_[date]模块调用features\_[date]模块建模预测最终结果

-   2017-06-26
    -   去掉了一个特征,修改了学习速率为0.02
    -   提交结果大概11600+,估计不少错误的结果提交

-   2017-06-29
    -   增加choose_best.py,在训练集上交叉验证测试所有的特征的组合,算出预测最高的
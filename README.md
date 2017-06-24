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


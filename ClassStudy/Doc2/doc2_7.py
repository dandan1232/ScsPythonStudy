# -*- coding: utf-8 -*-
# @Time    : 2023/3/16 13:53
# @Author  : Lindand
# @File    : doc2_7.py
# @Description :
# 现在8名体检人员的体重信息如下: (65.5, 70.2, 100.5, 45.5, 88.8, 55.5, 73.5, 67.8)，
# 请使用元组编写程序计算出方差，保留两位小数。
data = (65.5, 70.2, 100.5, 45.5, 88.8, 55.5, 73.5, 67.8)

# 计算均值
mean = sum(data) / len(data)

# 计算方差
variance = sum((x - mean) ** 2 for x in data) / len(data)

# 打印结果
print("方差为：{:.2f}".format(variance))

# -*- coding: utf-8 -*-
# @Time    : 2023/6/12 23:44
# @Author  : Lindand
# @File    : doc2_7.py
# @Description :
# 现在8名体检人员的体重信息如下: (65.5, 70.2, 100.5, 45.5, 88.8, 55.5, 73.5, 67.8)，
# 请使用元组编写程序计算出方差，保留两位小数。

tup = (65.5, 70.2, 100.5, 45.5, 88.8, 55.5, 73.5, 67.8)

avg = sum(tup) / len(tup)
num = sum((i - avg) ** 2 for i in tup) / len(tup)
print(format(num, ".2f"))
print("{:.2f}".format(num))

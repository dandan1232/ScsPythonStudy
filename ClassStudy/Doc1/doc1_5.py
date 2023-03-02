# -*- coding: utf-8 -*-
# @Time    : 2023/3/2 9:49
# @Author  : Lindand
# @File    : doc1_5.py
# @Description :
# 5.	编写程序让用户输入平面上两个点的坐标，计算该两点间的距离。

import math

a1 = float(input("请输入a1的横坐标:"))
a2 = float(input("请输入a1的纵坐标:"))
a3 = float(input("请输入a2的横坐标:"))
a4 = float(input("请输入a2的纵坐标:"))
if a1 > a3:
    x = a1 - a3
elif a1 < a3:
    x = a3 - a1
if a2 > a4:
    y = a2 - a4
elif a2 < a4:
    y = a4 - a2
d = math.sqrt(x * x + y * y)
print(x, y)
print("两个点的距离是%d" % d)

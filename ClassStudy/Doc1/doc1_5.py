# -*- coding: utf-8 -*-
# @Time    : 2023/3/2 9:49
# @Author  : Lindand
# @File    : doc1_5.py
# @Description :
# 5.	编写程序让用户输入平面上两个点的坐标，计算该两点间的距离。

import math

# 获取用户输入的点坐标
x1 = float(input("请输入第一个点的x坐标："))
y1 = float(input("请输入第一个点的y坐标："))
x2 = float(input("请输入第二个点的x坐标："))
y2 = float(input("请输入第二个点的y坐标："))

# 计算两点间的距离
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# 输出结果
print("两点间的距离为：", distance)


# -*- coding: utf-8 -*-
# @Time    : 2023/3/16 13:40
# @Author  : Lindand
# @File    : doc2_2.py
# @Description :编写一个程序，提示用户输入三角形的三个顶点(x1，y1)、（x2，y2）、（x3，y3），
# 然后计算三角形面积，这里假定输入的三个点能构成三角形。将面积输出到屏幕，要求输出占7列，保留2位小数，左对齐。

import math

# 获取用户输入
x1, y1 = map(float, input("请输入第一个点的坐标（以逗号分隔）：").split(","))
x2, y2 = map(float, input("请输入第二个点的坐标（以逗号分隔）：").split(","))
x3, y3 = map(float, input("请输入第三个点的坐标（以逗号分隔）：").split(","))

# 计算三角形面积
a = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
b = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
c = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

# 输出结果
print("{:<7}{:>7.2f}".format("面积：", area))


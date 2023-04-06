# -*- coding: utf-8 -*-
# @Time    : 2023/4/6 14:10
# @Author  : Lindand
# @File    : doc5_4.py
# @Description :
# 从键盘分别输入3个XOY二维平面内某三角形的顶点坐标（6个浮点数），在此基础上计算三角形的面积和周长。如果不能构成三角形需要提示错误信息。

import math

# 从键盘输入三角形的三个顶点坐标
x1, y1 = map(float, input("请输入第1个顶点坐标，以逗号分隔：").split(","))
x2, y2 = map(float, input("请输入第2个顶点坐标，以逗号分隔：").split(","))
x3, y3 = map(float, input("请输入第3个顶点坐标，以逗号分隔：").split(","))

# 计算三角形的三条边长
a = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
b = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
c = math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)

# 判断是否能构成三角形
if a + b > c and a + c > b and b + c > a:
    # 计算半周长和面积
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    # 计算周长
    perimeter = a + b + c

    # 输出结果
    print("三角形的面积为：", area)
    print("三角形的周长为：", perimeter)
else:
    # 不能构成三角形，输出错误信息
    print("无法构成三角形，请重新输入。")

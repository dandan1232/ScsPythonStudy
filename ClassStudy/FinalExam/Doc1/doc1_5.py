# -*- coding: utf-8 -*-
# @Time    : 2023/6/12 21:02
# @Author  : Lindand
# @File    : doc1_5.py
# @Description :编写程序让用户输入平面上两个点的坐标，计算该两点间的距离。

'''导包，pow用法，设为int值'''
import math

num1 = input("1(,):")
num2 = input("2(,):")
x1, y1 = (num1.split(","))
x2, y2 = (num2.split(","))
x1 = int(x1)
x2 = int(x2)
y2 = int(y2)
y1 = int(y1)
h = math.sqrt(math.pow(x1 - x2,2) + pow(y1 - y2,2))
print(h)

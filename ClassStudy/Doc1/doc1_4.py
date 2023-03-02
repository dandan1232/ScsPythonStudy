# -*- coding: utf-8 -*-
# @Time    : 2023/3/2 9:47
# @Author  : Lindand
# @File    : doc1_4.py
# @Description :
# 一只大象口渴了，要喝20升水才能解渴，但现在只有一个深h厘米，底面半径为r厘米的小圆桶(h和r都是整数)。
# 问大象至少要喝多少桶水才会解渴。编写程序输入半径和高度，输出需要的桶数（一定是整数）。

import math

h = input("输入高度h:")
r = input("输入半径r:")
a = math.pi * int(r) * int(r) * int(h)
b = 20000 / a
m = math.ceil(b)
print("桶数:%d" % m)

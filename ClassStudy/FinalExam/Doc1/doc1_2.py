# -*- coding: utf-8 -*-
# @Time    : 2023/6/12 20:37
# @Author  : Lindand
# @File    : doc1_2.py
# @Description :从键盘输入四个整数，并输出其中最大的数。

a = int(input("1:"))
b = int(input("2:"))
c = int(input("3:"))
d = int(input("4:"))
max = a
if b > max:
    max = b
if c > max:
    max = c
if d > max:
    max = d
print(max)

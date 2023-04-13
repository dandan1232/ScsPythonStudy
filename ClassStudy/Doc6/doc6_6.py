# -*- coding: utf-8 -*-
# @Time    : 2023/4/13 14:14
# @Author  : Lindand
# @File    : doc6_6.py
# @Description :求用于计算 S = a + aa + aaa + ... + a...a（n 个 a）值。
# 其中a是一个数字。a和n都是由键盘输入。例如：求S=2+22+222+2222+22222+222222, 那么a=2且n=6 。
a = int(input("请输入数字 a："))
n = int(input("请输入数字 n："))

total = 0
for i in range(1, n + 1):
    num = int(str(a) * i)
    total += num

print("S =", total)

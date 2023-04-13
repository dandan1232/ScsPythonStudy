# -*- coding: utf-8 -*-
# @Time    : 2023/4/13 13:39
# @Author  : Lindand
# @File    : doc6_3.py
# @Description :
# 用 * 输出一个正六边形。输入一个整数n代表输出的正六边形的边的长度(*的数目)，例如输入n = 3，输出：
# *   *   *
# *   *   *   *
# *   *   *   *   *
# *   *   *   *
# *   *   *
n = int(input("请输入数字n:"))
for i in range(n, 2 * n):
    if i <= 2 * n - 1:
        print((2 * n - 1 - i) * ' ', end='')
    print(i * ' *')
a = 1
for i in range(2 * n - 2, n - 1, -1):
    while i >= 2:
        print(a * ' ', end='')
        a += 1
        break
    print(i * ' *')


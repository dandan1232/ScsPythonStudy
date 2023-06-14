# -*- coding: utf-8 -*-
# @Time    : 2023/6/14 9:40
# @Author  : Lindand
# @File    : Trianle.py
# @Description :
n = int(input("请输入图形的行数: "))
for i in range(0, n):
    # for j in range(0, 10 - 1):
    #     print(" ", end=' ')
    for j in range(0, 2 * i + 1):
        print("*", end=' ')
    print("\n")

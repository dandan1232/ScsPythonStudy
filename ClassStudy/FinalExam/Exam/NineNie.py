# -*- coding: utf-8 -*-
# @Time    : 2023/6/14 10:47
# @Author  : Lindand
# @File    : NineNie.py
# @Description :


for i in range(1, 10):
    for j in range(1, i + 1):
        print("{0}*{1}={2}".format(i, j, i * j), end="\t")
    print()

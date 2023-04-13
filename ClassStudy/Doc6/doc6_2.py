# -*- coding: utf-8 -*-
# @Time    : 2023/4/13 13:35
# @Author  : Lindand
# @File    : doc6_2.py
# @Description :
# 输出一个乘法表。要求输入一个整数n,输出n*n的乘法表，乘法表打印出来为下三角样式，格式工整。例： 输入n=4。输出：
# 1    2    3    4
# 1	1
# 2   2    4
# 3   3    6    9
# 4   4    8    12   16
# 提示：可以使用print(i, end=’\t’)或print(‘%4d’% i)控制输出的数据格式。
n = int(input("请输入一个整数 n："))

# 输出表头
print(end='\t')
for i in range(1, n + 1):
    print(i, end='\t')
print()

# 输出表格
for i in range(1, n + 1):
    print(i, end='\t')
    for j in range(1, i + 1):
        print(i * j, end='\t')
    print()

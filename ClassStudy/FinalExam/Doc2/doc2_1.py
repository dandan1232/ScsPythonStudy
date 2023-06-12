# -*- coding: utf-8 -*-
# @Time    : 2023/6/12 21:17
# @Author  : Lindand
# @File    : doc2_1.py
# @Description :从键盘输入一个3位整数，请编写程序计算三位整数的各位数字之和，并输出到屏幕上，要求输出占4列，右对齐。

num = int(input("3位整数："))
a = num // 100
b = (num % 100)// 10
c = num % 10
print(a,b,c)
print(format(a + b + c, ">4"))

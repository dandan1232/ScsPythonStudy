# -*- coding: utf-8 -*-
# @Time    : 2023/6/12 20:32
# @Author  : Lindand
# @File    : doc1_1.py
# @Description :从键盘输入两个正整数 a 和 b ，计算并输出 a 除以 b 的商和余数


num1 = input("输入数字1：")
num2 = input("输入数字2：")
num1 = int(num1)
num2 = int(num2)
a, b = divmod(num1, num2)
print(a, b)

# -*- coding: utf-8 -*-
# @Time    : 2023/6/12 21:11
# @Author  : Lindand
# @File    : doc1_6.py
# @Description :产生一个随机3位正整数，并将该整数的数字首尾互换输出，例如：157 互换后为 751。

'''随机数产生用random.randint,divmod中间用，'''
import random

num = random.randint(100, 999)
print(num)
a, b = divmod(num, 100)
b, c = divmod(b, 10)
num1 = c * 100 + b * 10 + a
print(num1)

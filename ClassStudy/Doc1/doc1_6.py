# -*- coding: utf-8 -*-
# @Time    : 2023/3/2 9:51
# @Author  : Lindand
# @File    : doc1_6.py
# @Description :
# 产生一个随机3位正整数，并将该整数的数字首尾互换输出，例如：157 互换后为 751。

import random

a = random.randint(100, 999)
b = (a // 100)
c = (a // 10 % 10)
d = (a % 10)
r = d * 100 + c * 10 + b
print("随机数%d " % a)
print("反转后%d" % r)

# -*- coding: utf-8 -*-
# @Time    : 2023/6/14 9:33
# @Author  : Lindand
# @File    : Caclu.py
# @Description :编程实现输出[1,100]之间所有能被7整除但不能被3整除的数，并输出它们的乘积。
calu = 1
for i in range(1, 101):
    if i % 7 == 0 and i % 3 != 0:
        print(i)
        calu = i * calu
print(calu)

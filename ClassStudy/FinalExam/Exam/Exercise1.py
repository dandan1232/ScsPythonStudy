# -*- coding: utf-8 -*-
# @Time    : 2023/6/13 19:23
# @Author  : Lindand
# @File    : Exercise1.py
# @Description :
# 编写一个函数 factor，传入一个整数 n， 返回这个数的阶乘。比如传入 4， 则计算 4！,返回的值为 24。


def factor(n):
    if n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


result = factor(4)
print(result)

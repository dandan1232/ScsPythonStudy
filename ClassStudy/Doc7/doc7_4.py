# -*- coding: utf-8 -*-
# @Time    : 2023/4/20 13:39
# @Author  : Lindand
# @File    : doc7_4.py
# @Description :如果一个素数可以写成2p-1形式，其中p是一个正整数，那么该数就称作梅森素数。
# 请编写一个函数判断一个素数是否是梅森素数，如果是，则返回p的值，否则返回-1。
# 并编写测试程序找出1000以内的所有梅森素数输出到屏幕上，要求输出格式如下：
# P(占3列右对齐)   2p-1 (占4列右对齐)     # 此行不需要输出
# 2        3
# 3        7
# 5        31


def is_prime(n):
    """
    判断一个整数是否为素数。
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_mersenne_prime(p):
    """
    判断一个素数是否为梅森素数，是则返回p的值，否则返回-1。
    """
    mersenne_num = 2 ** p - 1
    if is_prime(mersenne_num):
        return p
    else:
        return -1




# 输出1000以内的所有梅森素数
# print("{:>3s} {:>4s}".format("P", "2p-1"))
for p in range(2, 32):
    if is_mersenne_prime(p) != -1:
        print("{:3d} {:4d}".format(p, 2 ** p - 1))

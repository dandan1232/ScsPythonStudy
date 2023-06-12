# -*- coding: utf-8 -*-
# @Time    : 2023/6/13 0:40
# @Author  : Lindand
# @File    : doc3_4.py
# @Description :用筛法求500 之内的所有质数，并打印输出所有的质数，每行输出5个质数。
'''不会'''
import math


def num(n):
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.sqrt(n) + 1)):
        if is_prime[i]:
            for j in range(i ** 2, n, i):
                is_prime[j] = False
    return [i for i in range(n) if is_prime[i]]


primes = num(500)
for i in range(len(primes)):
    if i % 5 == 0:
        print()
    print(primes[i], end=",")

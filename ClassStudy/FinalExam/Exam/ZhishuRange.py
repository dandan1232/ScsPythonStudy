# -*- coding: utf-8 -*-
# @Time    : 2023/6/14 11:13
# @Author  : Lindand
# @File    : ZhishuRange.py
# @Description :

# 100-200内所有的质数
import math


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if i % num == 0:
            return False
    return True


primes = []
for num in range(100, 201):
    if is_prime(num):
        primes.append(num)

count = 0
for prime in primes:
    print(prime, end=" ")
    count += 1
    if count % 10 == 0:
        print()

# 100以内的质数
num = []
for i in range(2, 101):
    for j in range(2, i):
        if (i % j == 0):
            break
    else:
        num.append(i)
print(num)



# -*- coding: utf-8 -*-
# @Time    : 2023/3/23 14:01
# @Author  : Lindand
# @File    : doc3_4.py
# @Description :用筛法求500 之内的所有质数，并打印输出所有的质数，每行输出5个质数。


def test(n):
    # 输入一个正整数n，返回一个包含所有小于n的质数的列表。
    is_prime = [True] * n  # 初始时假设所有数字都是质数
    is_prime[0] = is_prime[1] = False  # 0和1不是质数
    for i in range(2, int(n ** 0.5) + 1):  # 从2到sqrt(n)遍历
        if is_prime[i]:  # 如果i是质数
            for j in range(i ** 2, n, i):  # 将i的倍数标记为非质数
                is_prime[j] = False
    return [i for i in range(n) if is_prime[i]]


primes = test(500)
for i in range(len(primes)):
    if i % 5 == 0:  # 每行输出5个质数
        print()
    print(primes[i], end=' ')

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
from math import log2


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


# 从键盘中读取一个整数
n = int(input("请输入一个整数："))

# 判断这个整数是否为梅森素数
if is_prime(n):
    p = int(log2(n + 1))
    if is_mersenne_prime(p) == p:
        print(f"{n}是梅森素数，p={p}")
    else:
        print(f"{n}不是梅森素数(-1)")
else:
    print(f"{n} 不是素数")

# 输出1000以内的所有梅森素数
# print("{:>3s} {:>4s}".format("P", "2p-1"))
print("1000以内的所有梅森素数如下:")
for p in range(2, 32):
    if is_mersenne_prime(p) != -1:
        print("{:3d} {:4d}".format(p, 2 ** p - 1))

'''
这个代码中，首先使用 input 函数从键盘中读取一个整数，并将它保存在变量 n 中。
接着，调用之前定义的 is_prime 函数来判断这个整数是否为素数。
如果是素数，则使用公式 $p=\log_2(n+1)$ 计算出对应的梅森素数的p值，并调用 is_mersenne_prime 函数来判断这个素数是否为梅森素数。
如果是梅森素数，就输出梅森素数的p值；否则输出不是梅森素数的信息。如果输入的数不是素数，则输出不是素数的信息。
由于梅森素数的指数p很大，超过了Python的整数范围，因此此处只输出了指数小于32的梅森素数。
'''
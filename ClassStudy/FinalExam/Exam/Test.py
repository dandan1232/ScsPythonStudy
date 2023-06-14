# -*- coding: utf-8 -*-
# @Time    : 2023/6/14 9:01
# @Author  : Lindand
# @File    : Test.py
# @Description :

# x = 2
# y = 3
#
# x *= y + 5
#
# print(x)
#
# c = 4.5 // 2
# print(c)
# print(type(c))
#
# # x="Python";y=2;print(x+y)
#
# print(2 ** 3 ** 2)  # 2**(3**2)=2**9=512
# print(pow(6561, 1 / 4))

import math

n = 0
for m in range(101, 201, 2):
    # k=int(math.sqrt(m))
    # print("+++",k)
    for i in range(2, m):
        if m % i == 0: break
    if n % 10 == 0: print()
    print('%d' % m, end=' ')
    n += 1

n = int(input("请输入图形的行数: "))
for i in range(0, n):
    # for j in range(0, 10 - 1):
    #     print(" ", end=' ')
    for j in range(0, 2 * i + 1):
        print("*", end=' ')
    print("\n")

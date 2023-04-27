# -*- coding: utf-8 -*-
# @Time    : 2023/4/27 13:48
# @Author  : Lindand
# @File    : doc8_3.py
# @Description :
# 编写一个函数，用于计算整数m所有因子（包括1和m）之和，假设表示为φ(m)。
# 若有两个整数m<n，且φ(m)=φ(n)=m+n+1，则m和n称为拟互满数。
# 要求找出40~200之间的所有拟互满数

# 首先创建一个空列表 factors，然后从 2 开始迭代到 m，如果 i 是 m 的因子，则将其添加到 factors 列表中。
# 最后，使用 sum 函数来计算 factors 列表中所有元素的和，即为整数 m 所有因子之和 φ(m)
def phi(m):
    factors = [1]
    for i in range(2, m + 1):
        if m % i == 0:
            factors.append(i)
    return sum(factors)

for m in range(40, 200):
    n = phi(m) - m - 1
    if n > m and phi(n) == m + n + 1:
        print("拟互满数: ", m, n)


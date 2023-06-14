# -*- coding: utf-8 -*-
# @Time    : 2023/6/14 10:43
# @Author  : Lindand
# @File    : GongYinNumber.py
# @Description :

def gcd_exhaustive(a, b):
    # 确保a是较小的数
    if a > b:
        a, b = b, a

    # 从较小数开始逆向遍历
    for i in range(a, 0, -1):
        if a % i == 0 and b % i == 0:
            return i

    return 1  # 如果没有公因数，则返回1


a = 24
b = 36

result = gcd_exhaustive(a, b)
print(result)  # 输出: 12

# -*- coding: utf-8 -*-
# @Time    : 2023/4/20 13:32
# @Author  : Lindand
# @File    : doc7_1.py
# @Description :
# 编写一个函数，计算一个整数的所有因子之和，其中因子不包括整数本身，
# 并编写测试程序，在测试程序中输入整数，输出整数的所有因子之和。
# 例如：输入8，调用该函数之后，返回结果为7。

def factor_sum(n):
    """
    计算一个整数的所有因子之和，不包括整数本身。
    """
    factors = []
    for i in range(1, n):
        if n % i == 0:
            factors.append(i)
    return sum(factors)


# 测试程序
if __name__ == '__main__':
    n = int(input("请输入一个整数："))
    print("该整数的所有因子之和为：", factor_sum(n))

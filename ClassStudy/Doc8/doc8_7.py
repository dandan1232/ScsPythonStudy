# -*- coding: utf-8 -*-
# @Time    : 2023/4/27 13:52
# @Author  : Lindand
# @File    : doc8_7.py
# @Description :
# 用递归方法计算下列多项式函数的值：p(x,n)=x-x2+x3-x4+……+(-1)n-1xn  (n>0)
# 编写测试程序，从键盘输入x和n的值，打印p(x,n)的值。如果x=3.5, n=300呢？

import sys

# 多项式的项数非常大，递归计算可能会导致堆栈溢出，因此需要增加递归深度限制
sys.setrecursionlimit(10000)  # 设置递归深度限制为10000


def p(x, n):
    if n == 1:
        return x
    else:
        return x ** n - p(x, n - 1)


# 测试
x = float(input("请输入x的值："))
n = int(input("请输入n的值："))
result = p(x, n)
print("p(x,n)的值为：", result)

# 定义了函数p(x, n)，使用递归方法计算多项式函数的值。
# 其中，x表示多项式中的变量，n表示多项式的项数。
# 当项数n等于1时，函数返回变量x的值；当项数n大于1时，函数返回变量x的n次幂减去p(x, n-1)的值，即上一项的值

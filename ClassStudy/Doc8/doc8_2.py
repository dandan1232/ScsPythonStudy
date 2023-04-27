# -*- coding: utf-8 -*-
# @Time    : 2023/4/27 13:43
# @Author  : Lindand
# @File    : doc8_2.py
# @Description :
# 编写一个求阶乘的函数，再编写一个函数求组合数Cm n，其中Cm n=(m!)/(n!(m-n)!)。编写测试程序，要求用户输入m和n的值（n<m），输出结果。

def Munti(n):  # 求阶乘
    if n == 1:
        return 1
    else:
        return n * (Munti(n - 1))


def Getsum(m, n):  # 求组合数
    return (Munti(m) / (Munti(n) * Munti(m - n)))


m, n = map(int, input("输入m和n:").split())
print("%d" % (Getsum(m, n)))


# Munti(n) 函数是用来计算 n 的阶乘，采用递归的方式实现。
# Getsum(m,n) 函数是用来计算组合数 C(m,n)，采用调用 Munti(n) 函数的方式实现。
# m,n=map(int,input("输入m和n:").split()) 用来从用户输入中获取 m 和 n 的值。
# print("%d"%(Getsum(m,n))) 用来输出计算结果。
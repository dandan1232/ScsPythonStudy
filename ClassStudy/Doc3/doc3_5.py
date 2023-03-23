# -*- coding: utf-8 -*-
# @Time    : 2023/3/23 14:08
# @Author  : Lindand
# @File    : doc3_5.py
# @Description :
# 编写程序，完成500以内任意一个合数的质因数分解。
# 让用户输入一个500以内的合数，找出其所有质因数，并按照质因数乘法的形式输出，例如，60=2*2*3*5

'''在这个程序中，我们使用了一个名为 fenjie 的函数来计算质因数。
每次找到最小的质因数，将其添加到因子列表中，并将原始数除以该质因数，不断迭代直到原始数变为1为止。
最后，将所有因子按照乘法的形式输出即可。'''


def fenjie(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


'''在这个程序中，首先定义了一个名为 is_prime 的函数，用于检查一个数是否为质数。
从2到该数的平方根之间的所有数进行遍历，并检查是否有数能够整除该数。
如果存在这样的数，该数就不是质数。如果所有可能的数都不能整除该数，那么该数就是质数。'''


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


'''在程序的主体中，要求用户输入一个合数。
如果用户输入的数不在500以内，或者不是一个合数（例如素数），则程序会输出一条错误消息并结束。
否则，我们就调用 fenjie 函数来计算质因数，并将结果输出。'''

num = int(input("请输入一个500以内的合数: "))

if num < 1 or num > 500:
    print("输入有误！该数超出范围啦！！")
else:
    if is_prime(num):
            print("输入有误！该数为质数")
    else:
        factors = fenjie(num)
        print(f"{num}=", end="")
        for i, factor in enumerate(factors):
            if i == len(factors) - 1:
                print(factor)
            else:
                print(f"{factor}*", end="")

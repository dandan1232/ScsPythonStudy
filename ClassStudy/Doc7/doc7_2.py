# -*- coding: utf-8 -*-
# @Time    : 2023/4/20 13:34
# @Author  : Lindand
# @File    : doc7_2.py
# @Description :编写一个函数，将一个整数的各位数字对调，
# 要求使用元组参数实现，并编写测试程序，在测试函数中输入整数和输出新的整数。
# 例如：输入123，调用该函数之后，得到结果为321。

def swap_digits(n):
    """
    将一个整数的各位数字对调，返回新的整数。
    """
    digits = []
    while n > 0:
        digits.append(n % 10)
        n //= 10
    new_num = 0
    for digit in digits:
        new_num = new_num * 10 + digit
    return new_num


# 测试程序
if __name__ == '__main__':
    n = int(input("请输入一个整数："))
    new_num = swap_digits(n)
    print("新的整数为：", new_num)

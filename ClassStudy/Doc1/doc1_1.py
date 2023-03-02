# -*- coding: utf-8 -*-
# @Time    : 2023/3/2 9:28
# @Author  : Lindand
# @File    : doc1_1.py
# @Description :
# 1从键盘输入两个正整数 a 和 b ，计算并输出 a除以 b 的商和余数


if __name__ == '__main__':
    num1 = input("第一个数字:")
    num2 = input("第二个数字:")
    a, b = int(num1), int(num2)
    c, d = divmod(a, b)
    print("商:%d" % c + "余数为:%d" % d)

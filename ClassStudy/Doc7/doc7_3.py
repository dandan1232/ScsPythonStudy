# -*- coding: utf-8 -*-
# @Time    : 2023/4/20 13:36
# @Author  : Lindand
# @File    : doc7_3.py
# @Description :反素数指一个素数将其逆向拼写后也是一个素数的非回文数。
# 例如：17和71都是素数且都不是回文数，所以17和71都是反素数。
# 请编写一个函数判断一个数是否是反素数？并编写测试程序找出前30个反素数输出到屏幕上，要求每行输出8个数，每个数占5列，右对齐。
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


# 测试程序
if __name__ == '__main__':
    n = int(input("请输入一个整数："))
    new_num = swap_digits(n)
    print("新的整数为：", new_num)


def is_antiprime(n):
    """
    判断一个数是否为反素数。
    """
    reversed_n = swap_digits(n)
    return is_prime(n) and is_prime(reversed_n) and n != reversed_n and not str(n).startswith('0')


# 输出前30个反素数
count = 0
num = 10
print("输出前30个反素数:")
while count < 30:
    if is_antiprime(num):
        print("{:5d}".format(num), end="")
        count += 1
        if count % 8 == 0:
            print()
    num += 1

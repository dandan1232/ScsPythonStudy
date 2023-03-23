# -*- coding: utf-8 -*-
# @Time    : 2023/3/23 14:19
# @Author  : Lindand
# @File    : doc3_6.py
# @Description :
# 随机生成一个长度是100的整数列表，每个元素是100以内的正整数，使用遍历方法求该列表中不同的质数，
# 并求出该列表中有多少个质数可以表达为该列表中另外两个质数的和


import random

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


'''接下来，定义了一个名为 find_prime_numbers 的函数，用于遍历输入的列表并找出其中的所有质数。
这个函数利用了 is_prime 函数来判断每个数是否为质数，并使用一个集合来存储所有找到的质数。'''


def find_prime_numbers(lst):
    primes = set()
    for num in lst:
        if is_prime(num):
            primes.add(num)
    return primes


'''然后，我们定义了一个名为 find_sum_of_primes 的函数，用于找出列表中可以表示为另外两个质数之和的质数的数量。
首先，我们使用 find_prime_numbers 函数来找出列表中的所有质数。
然后，我们遍历其中的每对质数，并检查它们的和是否也是一个质数。
如果是，我们就增加计数器的值，表示找到了一个可以表示为另外两个质数之和的质数。
需要注意的是，我们只需要找到一个与该质数的和相等的质数即可，因此我们使用了一个 break 语句来提前结束内层循环。'''


def find_sum_of_primes(lst):
    primes = find_prime_numbers(lst)
    count = 0
    for prime1 in primes:
        for prime2 in primes:
            if prime1 != prime2 and prime1 + prime2 in primes:
                count += 1
                break
    return count


'''最后，我们生成一个长度为100的随机整数列表，并分别调用 find_prime_numbers 和 find_sum_of_primes 函数来计算所需的结果。
程序会输出生成的列表、不同的质数数量和可以表示为另外两个质数之'''

lst = [random.randint(1, 100) for _ in range(100)]
print(f"生成的随机整数列表为：{lst}")
primes = find_prime_numbers(lst)
print(f"该列表中不同的质数有 {len(primes)} 个")
count = find_sum_of_primes(lst)
print(f"该列表中有 {count} 个质数可以表示为该列表中另外两个质数的和")

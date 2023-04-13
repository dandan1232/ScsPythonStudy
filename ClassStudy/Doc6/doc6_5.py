# -*- coding: utf-8 -*-
# @Time    : 2023/4/13 13:52
# @Author  : Lindand
# @File    : doc6_5.py
# @Description :验证哥德巴赫猜想：“任何大于2的偶数，都是两个质数之和。”
# 提示用户输入一个大于2的偶数，把它分成两个质数，输出结果。（用循环嵌套，不用函数）
# （这里只是对有限范围内的数，用计算机加以验证，不算严格的证明。哥德巴赫猜想是一个古老而著名的数学难题，迄今未得出最后的理论证明。）


while True:
    n = int(input("请输入一个大于2的偶数："))
    if n <= 2 or n % 2 != 0:
        print("输入不合法，请重新输入。")
        continue

    is_valid = False
    for i in range(2, n):
        if i > n - i:  # 遍历到一半即可停止
            break

        is_prime_i = True
        for j in range(2, i):
            if i % j == 0:
                is_prime_i = False
                break

        is_prime_ni = True
        for j in range(2, n - i):
            if (n - i) % j == 0:
                is_prime_ni = False
                break

        if is_prime_i and is_prime_ni:  # 找到一组满足条件的质数
            print("{} = {} + {}".format(n, i, n - i))
            is_valid = True
            break

    if not is_valid:
        print("无法找到两个质数使得它们的和等于{}。".format(n))

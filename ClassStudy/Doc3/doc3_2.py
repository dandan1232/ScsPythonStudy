# -*- coding: utf-8 -*-
# @Time    : 2023/3/23 13:51
# @Author  : Lindand
# @File    : doc3_2.py
# @Description :已知一个整数列表，判断列表内容是否为回文，即无论正序还是倒序，列表的内容是否相同。

def is_huiwen(lst):
    # 获取列表长度
    n = len(lst)
    # 遍历列表前一半的元素
    for i in range(n // 2):
        # 判断当前元素与对应位置上的元素是否相同
        if lst[i] != lst[n - i - 1]:
            return False
    # 如果循环执行完毕，说明列表是回文的
    return True

lst1 = [4, 8, 7, 8, 4]
print(is_huiwen(lst1))  # 输出 True

lst2 = [1,4,8,2,3,1]
print(is_huiwen(lst2))  # 输出 False


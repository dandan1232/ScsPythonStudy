# -*- coding: utf-8 -*-
# @Time    : 2023/3/23 13:58
# @Author  : Lindand
# @File    : doc3_3.py
# @Description :现有列表[35, 46, 57, 13, 24, 35, 99, 68, 13, 79, 88, 46]，请编写程序将其中重复的元素去除，并按从小到大的顺序排列后输出。

before_list = [35, 46, 57, 13, 24, 35, 99, 68, 13, 79, 88, 46]
# set除了原始列表中的重复元素，sorted按从小到大的顺序进行了排序
after_list = sorted(list(set(before_list)))

print(after_list)

# -*- coding: utf-8 -*-
# @Time    : 2023/3/23 15:24
# @Author  : Lindand
# @File    : doc3_7.py
# @Description :
# 编写程序让用户输入两个字符串（一定是小写字母组成），判断两个字符串是否同构。
# 如果有两个字符串，其中一个字符串的字符重新排列后，能变成另一个字符串，那么称为同构

from collections import Counter

str1 = input("请输入第一个字符串: ")
str2 = input("请输入第二个字符串: ")

# 使用 Counter 函数统计字符出现次数
count1 = Counter(str1)
count2 = Counter(str2)

# 将两个字符串转换成集合
set1 = set(str1)
set2 = set(str2)

# 判断两个集合是否相等,并且判断两个计数器是否相等
if set1 == set2 and count1 == count2 and  'a' <= str1 <= 'z':
    print("两个字符串是否同构")
else:
    print("两个字符串不是否同构或者输出有误哦（必须输入纯小写英文字母串）")

# -*- coding: utf-8 -*-
# @Time    : 2023/4/20 13:44
# @Author  : Lindand
# @File    : doc7_5.py
# @Description :
# 编写一个函数实现排序。
# 从键盘依次输入10个字母（如果有大小写，需要区分），按照字母的ASCII码值分别进行从小到大、从大到小的排序，并输出排序的结果。
# 提示：可以使用字典按值排序。

def sort_letters(letters):
    """
    对字母列表进行排序，分别按照字母的ASCII码值从小到大和从大到小排序。
    """
    # 按照ASCII码值从小到大排序
    sorted_letters_asc = sorted(letters)
    # 按照ASCII码值从大到小排序
    sorted_letters_desc = sorted(letters, reverse=True)
    return sorted_letters_asc, sorted_letters_desc


# 从键盘依次输入10个字母，存储到列表中
letters = []
for i in range(10):
    letter = input("请输入第{}个字母：".format(i + 1))
    letters.append(letter)

# 对字母列表进行排序
sorted_letters_asc, sorted_letters_desc = sort_letters(letters)

# 输出排序结果
print("按照ASCII码值从小到大排序的结果为：")
print(sorted_letters_asc)
print("按照ASCII码值从大到小排序的结果为：")
print(sorted_letters_desc)

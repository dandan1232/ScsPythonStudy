# -*- coding: utf-8 -*-
# @Time    : 2023/3/16 13:52
# @Author  : Lindand
# @File    : doc2_6.py
# @Description :写一个程序处理用户输入的字符串，并按用户要求删除其中第n个字符，返回删除字符后的字符串。

def remove_char(s, n):
    # 判断n是否在字符串的索引范围内
    if n >= len(s):
        return "索引超出字符串范围！"
    # 删除字符串中第n个字符
    new_s = s[:n] + s[n+1:]
    return new_s

s = input('请输入一个字符串：')
n = int(input('请输入要删除的字符索引：'))
new_s = remove_char(s, n)
print(new_s)

# -*- coding: utf-8 -*-
# @Time    : 2023/5/4 13:41
# @Author  : Lindand
# @File    : doc9_2.py
# @Description :
# 编写程序实现文本文件的合并功能，有两个文本文件cat1.txt和cat2.txt，将cat2.txt文件中的内容添加到cat1.txt文件中，提示合并完成。

with open('date/cat1.txt', 'a') as cat1_file:
    with open('date/cat2.txt', 'r') as cat2_file:
        cat1_file.write(cat2_file.read())

print('合并完成')

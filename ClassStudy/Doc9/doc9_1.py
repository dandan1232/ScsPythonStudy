# -*- coding: utf-8 -*-
# @Time    : 2023/5/4 13:36
# @Author  : Lindand
# @File    : doc9_1.py
# @Description :
# 编写程序实现文本文件的复制功能，打开文本文件copy.txt，
# 在当前路径下新建一个new.txt文件，将copy.txt的内容复制到new.txt文件中，提示拷贝完成。

with open('date/copy.txt', 'r') as src_file:
    with open('new.txt', 'w') as dst_file:
        dst_file.write(src_file.read())

print('拷贝完成')

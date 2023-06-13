# -*- coding: utf-8 -*-
# @Time    : 2023/6/13 20:06
# @Author  : Lindand
# @File    : doc9_2.py
# @Description :编写程序实现文本文件的合并功能，有两个文本文件cat1.txt和cat2.txt，将cat2.txt文件中的内容添加到cat1.txt文件中，提示合并完成。


with open('date/cat2.txt','r') as src:
    with open('date/cat1.txt','a+') as dst:
        dst.write(src.read())
print("1")

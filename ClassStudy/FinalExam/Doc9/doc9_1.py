# -*- coding: utf-8 -*-
# @Time    : 2023/6/13 20:01
# @Author  : Lindand
# @File    : doc9_1.py
# @Description :
# 编写程序实现文本文件的复制功能，打开文本文件copy.txt，
# 在当前路径下新建一个new.txt文件，将copy.txt的内容复制到new.txt文件中，提示拷贝完成。


with open('date/copy.txt','r') as src:
    with open('date/new.txt','w') as copy:
        copy.write(src.read())
print("1")
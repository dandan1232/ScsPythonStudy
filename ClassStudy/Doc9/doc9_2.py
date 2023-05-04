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

# 使用两个 with 语句，用于自动管理文件的打开和关闭。
# 'a' 表示以追加模式打开文件，这样可以将cat2.txt中的内容添加到cat1.txt的末尾。
# read 和 write 方法也可以用于读取和写入文件内容，write 方法写入的内容会追加到cat1.txt的末尾。
# 运行程序后，会将cat2.txt中的内容添加到cat1.txt的末尾，并输出合并完成提示。
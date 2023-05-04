# -*- coding: utf-8 -*-
# @Time    : 2023/5/4 13:36
# @Author  : Lindand
# @File    : doc9_1.py
# @Description :
# 编写程序实现文本文件的复制功能，打开文本文件copy.txt，
# 在当前路径下新建一个new.txt文件，将copy.txt的内容复制到new.txt文件中，提示拷贝完成。

with open('date/copy.txt', 'r') as src_file:
    with open('date/new.txt', 'w') as dst_file:
        dst_file.write(src_file.read())

print('拷贝完成')

# 使用了两个 with 语句，用于自动管理文件的打开和关闭。
# open 函数用于打开文件，第一个参数为文件名，第二个参数为打开模式。
# 'r' 表示只读模式，'w' 表示写模式，如果文件不存在则创建文件。在 with 语句块中可以使用 read 和 write 方法来读取和写入文件内容。
# 运行程序后，会在当前路径下生成一个名为 new.txt 的文件，并将 copy.txt 的内容复制到这个文件中。程序会输出 拷贝完成 提示。

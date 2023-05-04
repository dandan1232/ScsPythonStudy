# -*- coding: utf-8 -*-
# @Time    : 2023/5/4 13:42
# @Author  : Lindand
# @File    : doc9_6.py
# @Description :
# 有一个100G的文件largefile.txt（这个文件目前没有100G，只是做模拟）。
# 实现一个程序，首先输出largefile.txt的行数，然后无限循环，每次要求用户键盘输入一个行号，然后立刻输出对应行的文本。
# 由于文件很大，不允许将文件内容全部放到内存中； 同时也不允许从头扫描文件，得到对应行的文本，因为这样速度太慢。
# （提示：用二进制模式打开文件，使用tell, seek等方法）。

# 定义 largefile.txt 文件路径
file_path = 'date/largefile.txt'

# 读取所有行的偏移量
offsets = []
with open(file_path, 'rb') as f:
    offset = 0
    offsets.append(offset)
    while True:
        line = f.readline()
        if not line:
            break
        offset += len(line)
        offsets.append(offset)

# 输出行数
print('行数：', len(offsets))

# 进入循环，输出指定行的文本内容
while True:
    try:
        line_num = int(input('请输入行号（输入-1退出）：'))
    except ValueError:
        print('输入的行号无效，请重新输入！')
        continue
    if line_num == -1:
        break
    elif line_num < 1 or line_num > len(offsets):
        print('输入的行号超出范围，请重新输入！')
        continue
    else:
        # 定位到对应行的偏移量并输出该行文本内容
        offset = offsets[line_num - 1]
        with open(file_path, 'rb') as f:
            f.seek(offset)
            line = f.readline().decode('utf-8')
        print(line.strip())

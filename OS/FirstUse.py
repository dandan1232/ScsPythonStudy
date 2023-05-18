# -*- coding: utf-8 -*-
# @Time    : 2023/5/15 13:50
# @Author  : Lindand
# @File    : FirstUse.py
# @Description :
# 编写一个python程序，有一块完整的memory，有很多的字符串，字符串命令格式为：a + 100KB（格式：字母 空格 加/减号 空格  数字；），
# 一个字母为一个进程，加减表示为进程的进出，要求使用操作系统的首次适应，输出内存中所有的外部碎块，输出单位为K，输出格式：编号+起始地址


memory_size = 2 * 1024  # 内存大小为2MB
memory = [None] * memory_size  # 初始化内存列表，每个元素代表1K内存块
external_fragments = []  # 外部碎片列表

# 用于从字符串命令中提取字母和数字的正则表达式
import re

command_pattern = re.compile(r'(\w)\s*([+-])\s*(\d+)KB')


# 用于打印外部碎片的函数
def print_external_fragments():
    print("外部碎片：")
    for i, block in enumerate(memory):
        if block is None:
            if i == 0 or memory[i - 1] is not None:
                print(f"{i}\t{i}K")
        elif i > 0 and memory[i - 1] is None:
            print(f"{i}\t{i}K")


# 从命令字符串中提取进程和内存大小
def parse_command(command):
    match = command_pattern.match(command)
    if match:
        process = match.group(1)
        operation = match.group(2)
        size = int(match.group(3))
        if operation == '-':
            size = -size
        return process, size
    else:
        return None, None


# 首次适应算法
def first_fit(process, size):
    start = None
    for i, block in enumerate(memory):
        if block is None:
            if start is None:
                start = i
            if i - start + 1 == size:
                for j in range(start, i + 1):
                    memory[j] = process
                return True
        else:
            start = None
    return False


# 处理命令字符串
def process_command(command):
    process, size = parse_command(command)
    if process is None:
        return
    if size > 0:
        if not first_fit(process, size):
            print(f"无法为进程{process}分配{size}K内存")
    else:
        for i, block in enumerate(memory):
            if block == process:
                if i == 0 or memory[i - 1] is not None:
                    external_fragments.append((i, i))
                if i == memory_size - 1 or memory[i + 1] is not None:
                    external_fragments[-1] = (external_fragments[-1][0], i)
                memory[i] = None


# 测试代码
commands = ['a + 100KB', 'b + 200KB', 'c + 50KB', 'd + 300KB', 'a - 100KB', 'e + 150KB', 'f + 50KB', 'c - 50KB']
for command in commands:
    process_command(command)
    print_external_fragments()

'''
首次适应：
Python 程序实现了首次适应算法来分配内存，即从内存的开始位置开始查找，找到第一个可以容纳该进程的内存块并进行分配。
如果没有找到可用内存块，则无法为该进程分配内存。
因此，上面的程序使用了首次适应算法来模拟内存中字符串的加减，可以根据命令字符串中的加减号，为进程分配或释放指定大小的内存块。
如果成功分配了内存，则将进程名写入内存块中，如果释放了内存，则将相应的内存块清空为 None。
因此，上面的程序使用了首次适应算法来模拟内存中字符串的加减。
'''
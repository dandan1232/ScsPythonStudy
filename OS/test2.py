# -*- coding: utf-8 -*-
# @Time    : 2023/5/15 14:42
# @Author  : Lindand
# @File    : test2.py
# @Description :编写一个python程序，有一块完整的memory，有很多的字符串，
# 字符串命令格式为：a + 100KB（格式：字母 空格 加/减号 空格  数字），一个字母为一个进程，加减表示为进程的进出，要求使用操作系统的首次适应，输出内存中所有的外部碎块，输出单位为K，输出格式：编号+起始地址，
# 采用如下数据结构：设为2字节，1K为一个点点，设置Memory为9K，需要4K，则给4K（就是4个点点）打叉，
# 释放后将打叉的点点还原，如此重复，就最后打印空白条，未被打叉的点点，实现这个，声明一个大的数组，
# 数组的用0 1表示，数组的位置从0开始，分配谁，就找到那个地方分个点，分配谁就分个点，释放就把点去掉，最后扫描所有空白地方，打印出起始点和长度

MEMORY_SIZE = 9 * 1024 // 2  # 内存大小，2字节为1K，单位为点点(一个小圆点)

memory = [0] * MEMORY_SIZE  # 内存，使用列表模拟

while True:
    command = input("请输入命令（格式：字母 空格 加/减号 空格 数字），退出请输入 q：")
    if command == "q":
        break

    process_id, op, size_str = command.split()
    size = int(size_str[:-2]) * 2  # 转换成点点数量

    if op == "+":
        # 分配内存
        allocated = False
        for i in range(len(memory) - size):
            if memory[i:i + size] == [0] * size:
                # 可以分配
                memory[i:i + size] = [1] * size
                print(f"成功分配 {size // 2}KB 内存给进程 {process_id}，起始地址为 {i // 2}。")
                allocated = True
                break

        if not allocated:
            print(f"分配内存给进程 {process_id} 失败，内存不足！")
    elif op == "-":
        # 释放内存
        start = int(size_str[:-2]) * 2
        end = start + len(process_id) * 2
        for i in range(start, end):
            memory[i] = 0
        print(f"成功释放进程 {process_id} 占用的内存。")

    # 输出所有外部碎片
    print("外部碎片：")
    start = None
    for i, m in enumerate(memory):
        if m == 0 and start is None:
            start = i
        elif m == 1 and start is not None:
            print(f"{start // 2}K - {(i - 1) // 2}K，长度为 {(i - start) // 2}K")
            start = None
    if start is not None:
        print(f"{start // 2}K - {(len(memory) - 1) // 2}K，长度为 {(len(memory) - start) // 2}K")


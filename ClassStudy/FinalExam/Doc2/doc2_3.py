# -*- coding: utf-8 -*-
# @Time    : 2023/6/12 23:01
# @Author  : Lindand
# @File    : doc2_3.py
# @Description :
# 请编写一个程序显示当前北京时间，要求显示格式如下：
# 当前时间是：几时：几分：几秒
# 输出示例：当前时间是： 14：26：32

from datetime import datetime

time = datetime.now()
current = time.strftime("%H:%M:%S")
print(current)

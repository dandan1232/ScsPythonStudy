# -*- coding: utf-8 -*-
# @Time    : 2023/3/16 13:46
# @Author  : Lindand
# @File    : doc2_3.py
# @Description :
# 请编写一个程序显示当前北京时间，要求显示格式如下：
# 当前时间是：几时：几分：几秒
# 输出示例：当前时间是： 14：26：32


import datetime

# 获取当前北京时间
now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8)))

# 格式化输出时间
time_str = now.strftime("当前时间是： %H:%M:%S")

# 打印输出结果
print(time_str)

# -*- coding: utf-8 -*-
# @Time    : 2023/5/18 13:52
# @Author  : Lindand
# @File    : Doc11_4.py
# @Description :设计一个课程类，包括课程编号、课程名称、任课教师、上课地点等成员，其中上课地点是私有的。
# 添加构造方法及显示课程信息的方法，最后在主模块中定义类的对象，测试所设计的方法并显示最后结果。

class Course:
    def __init__(self, course_id, course_name, teacher, location):
        self.course_id = course_id
        self.course_name = course_name
        self.teacher = teacher
        self.__location = location

    def display_info(self):
        print("课程编号:", self.course_id)
        print("课程名称:", self.course_name)
        print("任课教师:", self.teacher)
        print("上课地点:", self.__location)


# 创建课程对象并显示信息
course = Course("C001", "Python程序设计", "林丹丹", "数字中心201")
course.display_info()

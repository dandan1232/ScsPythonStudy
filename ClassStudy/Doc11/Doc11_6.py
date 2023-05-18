# -*- coding: utf-8 -*-
# @Time    : 2023/5/18 14:10
# @Author  : Lindand
# @File    : Doc11_6.py
# @Description :为五年级3班的同学创建一个类，属性包括学号、姓名、性别和年龄，班级容量是45，也即最多允许实例化45个同学。

class Student:
    class_capacity = 45
    student_count = 0

    def __init__(self, student_id, name, gender, age):
        self.student_id = student_id
        self.name = name
        self.gender = gender
        self.age = age

        Student.student_count += 1

        if Student.student_count > Student.class_capacity:
            raise ValueError("班级已满，无法再添加新的学生。")

    def display_info(self):
        print("学号:", self.student_id)
        print("姓名:", self.name)
        print("性别:", self.gender)
        print("年龄:", self.age)


# 实例化学生对象
student1 = Student(1, "林丹丹", "女", 8)
student2 = Student(2, "念安", "女", 13)
student3 = Student(3, "石二狗", "男", 19)
student4 = Student(4, "亦安", "女", 20)
student5 = Student(5, "阿正", "男", 6)

# 输出学生信息
student1.display_info()
student2.display_info()
student3.display_info()
student4.display_info()
student5.display_info()

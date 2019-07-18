#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Description: 工资结算系统
@author: xieziwei99
@Create Date: 2019/7/17
"""
from abc import ABCMeta, abstractmethod


# 通过指定metaclass=ABCMeta，使其成为抽象基类
class Employee(metaclass=ABCMeta):
    """员工，抽象类"""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        pass


class Manager(Employee):

    def get_salary(self):
        return 15000.0


class Programmer(Employee):

    def __init__(self, name, working_hour=0):
        super().__init__(name)
        self.working_hour = working_hour

    def get_salary(self):
        return 200.0 * self.working_hour


class Salesman(Employee):

    def __init__(self, name, sales=0.0):
        super().__init__(name)
        self.sales = sales

    def get_salary(self):
        return 1800.0 + self.sales * 0.05


class EmployeeFactory(object):
    """创建员工的工厂（工厂模式 - 通过工厂实现对象使用者和对象之间的解耦合）"""

    @staticmethod
    def create(emp_type: str, *args, **kwargs):
        if 'M' == emp_type:
            emp = Manager(*args, **kwargs)
        elif 'P' == emp_type:
            emp = Programmer(*args, **kwargs)
        elif 'S' == emp_type:
            emp = Salesman(*args, **kwargs)
        else:
            raise ValueError(f'{emp_type}：没有这种类型的员工')
        return emp


def main():
    employees = [
        EmployeeFactory.create('M', '曹操'),
        EmployeeFactory.create('P', '荀彧', 120),
        EmployeeFactory.create('P', '郭嘉', 85),
        EmployeeFactory.create('S', '典韦', 123000),
    ]
    for emp in employees:
        print(f'{emp.name}: {emp.get_salary()}元')


if __name__ == '__main__':
    main()

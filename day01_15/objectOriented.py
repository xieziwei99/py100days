'''
Created on 2019年06月10日
面向对象设计基础示例
@author: xieziwei99
'''

class Person(object):
    
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)

    # 静态方法
    @staticmethod
    def sayHello():
        print('Hello, I am one of Person')

def main():
    person = Person('王大锤', 12)
    person.play()
    person.age = 22
    person.play()
    Person.sayHello()
    # person.name = '白元芳'  # AttributeError: can't set attribute

if __name__ == '__main__':
    main()
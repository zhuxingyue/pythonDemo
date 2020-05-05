'''
python 中的类与对象创建

    python 中的类定义关键字class 函数关键字def，定义本类属性关键字self
'''


# 创建类，创建类属性
class People:
    name = None
    age = None
    sex = None

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def eat(self):
        print("人吃饭！")

    def getInfor(self):
        print("我的名字：", self.name)
        print("我的年龄：", self.age)
        print("我的性别：", self.sex)


people = People("li", 29, "女")
people.getInfor()

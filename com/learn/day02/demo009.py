'''
python 中的装饰器

    通过函数名称赋值给变量实现装饰器效果
'''


def test(fun):
    def f():
        print("定义: python函数装饰器")
        fun()
    return f


def testFun():
    print("运行函数")


testF = test(testFun)
testF()


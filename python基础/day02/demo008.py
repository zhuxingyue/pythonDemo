def test():
    print('python 中的函数测试！！！')
    # 无参无返回的函数
    test1()

    # 无参有返回的函数
    re = test2()
    print(re)

    # 有参无返回的函数
    test3("python")

    # 有参有返回的函数
    re = test4("python")
    print(re)


def test1():
    print("python 无参无返回的函数！！")


def test2():
    print("python 无参有返回的函数！！")
    return "返回值：python"


def test3(a):
    print(a, " 有参无返回的函数！！")


def test4(a):
    print(a, "有参有返回的函数！！")
    return "返回值：python"


test()

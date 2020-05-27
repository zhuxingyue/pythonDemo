# 创建元组
tuple_info = ("zhangsan", 18, 1.75)

# 元组中元素个数
con = tuple_info.count(18)
print(con)

# 元组中元素索引
index = tuple_info.index(1.75)
print(index)


"""
元组使用场景：
    1。作为函数的输入参数，返回值
    2。格式化字符串
"""

str = "名字：%s，年龄：%s，身高：%s" % tuple_info
print(str)

# 定义单个元素的元组
tuple_one = (12,)
print(type(tuple_one))

'''
python 中的数据结构
    分为：
        列表，元组，字典，集合
'''

# 列表：
lis = [1, 3, 5, 7, 8]
del lis[0]
print(lis)

lis.append(9)
print(lis)

lis.pop(lis[0])
print(lis)

lis.remove(lis[0])
print(lis)

# 元组
lis1 = (2, 4, 6, 8)
print(lis1)

# 字典
lis2 = {"a": 3, "b": 4, "c": 5}
a = lis2.keys()
print(a)

# 集合
lis3 = {"a", "b", "c"}
print(lis3)
lis3.add("d")
print(lis3)


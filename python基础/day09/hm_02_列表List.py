"""
列表的方法：
    添加： append， insert， extend
    删除： remove， clear，  pop
    del:关键字删除，如果使用del关键字删除，后续代码无法在使用这个变量
    统计： len，    count
    排序： sort，   reverse
"""

nameList = ["zhang", "li", "zhao"]

# 获取列表的索引
print(nameList.index("zhang"))

nameList[0] = "sun"

print(nameList)

# 在列表末尾添加数据
nameList.append("wang")

# 在指定位置插入数据
nameList.insert(1, "zhu")

# 将其他列表数据追加到指定列表末尾
tylist = ["孙悟空", "祝二弟"]
nameList.extend(tylist)
print(nameList)

# 删除列表中指定数据
nameList.remove("wang")

# 默认删除列表最后一个数据，传入参数指定删除对应索引数据
nameList.pop()
nameList.pop(1)

# 清空列表
nameList.clear()
print(nameList)

# del 关键字删除
tylist = ["孙悟空", "祝二弟"]
del tylist[0]
print(tylist)

nameList = ["zhang", "li", "zhao", "li"]
# 统计列表中有几个元素
con = len(nameList)
print(con)

# 统计列表中某个元素出现的次数
con = nameList.count("li")
print(con)

# 列表排序
lis = [1, 6, 2, 8, 3]
lis1 = ["zhang", "li", "wang"]

# 升序
# lis.sort()
# lis1.sort()

# 降序
# lis.sort(reverse=True)
# lis1.sort(reverse=True)

# 列表反转
lis.reverse()
lis1.reverse()
print(lis)
print(lis1)



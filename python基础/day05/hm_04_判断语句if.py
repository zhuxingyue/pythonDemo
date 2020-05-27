"""
判断语句：
    if
    if else
    if elif else
"""
a = int(input("请输入第一个数："))
b = int(input("请输入第二个数："))

if a == b:
    print("相等！")

if a == b:
    print("两数相等！")
else:
    print("两数不相等")

if a > b:
    print("a大")
elif a == b:
    print("相等")
else:
    print("b大")

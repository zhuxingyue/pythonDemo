"""
    循环嵌套：
        while 表达式：
            代码：
            while 表达式：
                代码
"""

"""

连续输出5行，打印：
*
**
***
"""
row = 1

while row <= 5:
    print("*" * row)
    row += 1

row = 1
while row <= 5:
    num = 1
    while num <= row:
        print("*", end="")
        num += 1
    print("")
    row += 1
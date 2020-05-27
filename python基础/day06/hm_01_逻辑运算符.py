"""
逻辑运算符：python中的逻辑运算符就3种
    and       与
    or        或
    not       非
"""
a = 10
b = 20
c = 30
if a < b and c > a:
    print("b最小")

if a > b or c > b:
    print("ce")

# 关系运算符
if a != b:
    print("a不等于b")

# 逻辑运算符
if not not b:
    print("阿斯顿看风景")

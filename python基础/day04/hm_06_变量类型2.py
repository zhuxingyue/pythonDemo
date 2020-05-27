"""
不同类型变量之间的运算：

"""
a = 3
b = 1.2
c = False

# bool类型True和其他类型相加运算，按照1运算；False，按0运算
print(a+b)
print(a+c)
print(b+c)


# 字符串和整数用* 号可以使字符串连续拼接
first_name = "张"
last_name = "三"
print(first_name * a)
print(last_name * a)

print((first_name+last_name)*a)

"""
continue 关键字跳出当前循环，进行下一次循环
continue使用时，continue之前需要修改循环条件否则会进入是循环
"""

i = 0

while i < 10:

    if i == 5:
        i += 1
        continue
    print("i如果是5跳过循环，进行下一个循环：i=%d" % i)
    i += 1
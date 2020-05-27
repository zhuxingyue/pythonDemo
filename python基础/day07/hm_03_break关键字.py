"""
break关键字终止当前循环

"""

i = 0
while i < 10:
    if i == 5:
        break
    print("i如果是5循环终止, i = %d" % i)
    i += 1

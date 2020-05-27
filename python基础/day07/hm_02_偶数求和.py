"""
偶数求和
0-100 之间的偶数求和
"""
sum = 0
i = 2

# while i <= 100:
#     sum += i
#     print(i)
#     print(sum)
#     i += 2

while i <= 100:
    if i % 2 == 0:
        sum += i
        print(i)
    i += 1
    print(sum)
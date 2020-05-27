"""
剪刀 = 1
石头 = 2
布   = 3

用户和电脑玩石头剪刀布，判断玩家的胜负
"""
import random

player = int(input("请出拳：（剪刀：1，石头：2，布：3）"))

# 随机整数
pc = random.randint(1, 3)

# 创建枚举类型
lis = ["剪刀", "石头", "布"]
enum = enumerate(lis, 1)

# 通过遍历赋值
for i, item in enum:
    if player == i:
        playerGame = item
    if pc == i:
        pcGame = item

# 胜利条件

if ((player == 1 and pc == 3)
        or (player == 2 and pc == 1)
        or (player == 3 and pc == 2)):

    print("电脑出拳是：%s 玩家出拳是：%s，获胜！！，太厉害了" % (pcGame, playerGame))
elif player == pc:
    print("电脑出拳是：%s 玩家出拳是：%s，平局！！，再接再厉" % (pcGame, playerGame))
else:
    print("电脑出拳是：%s 玩家出拳是：%s，失败！！，太菜了" % (pcGame, playerGame))

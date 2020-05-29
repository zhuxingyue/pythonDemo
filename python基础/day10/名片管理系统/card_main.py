from day10.名片管理系统.card_tools import add_card, display_all, search_card

while True:
    print("****************************")
    print("欢迎使用【名片管理系统】v1.0")
    print()
    print("1.新增名片")
    print("2.显示全部")
    print("3.查询名片")
    print()
    print("0.推出系统")
    print("****************************")

    func_num = input("请选择功能:")
    func_num = int(func_num)

    if func_num == 0:
        break
    elif func_num == 1:
        add_card()
    elif func_num == 2:
        print("显示名片内容：")
        display_all()
    elif func_num == 3:
        search_card()
    else:
        print("输入的数字：%d功能错误，没有该功能" % func_num)

from day10.名片管理系统.card_display import display_more, display_one

cards = []


def add_card():
    """新增名片"""
    name = input("请输入姓名：")
    mobile = input("请输入电话：")
    qq = input("请输入qq：")
    email = input("请输入邮箱：")

    card_info = {"name": name, "mobile": mobile, "qq": qq, "email": email}
    cards.append(card_info)


def display_all():
    """显示全部名片"""
    display_more(cards)


def search_card():
    """查询名片"""
    name = input("请输入需要查询的名字：")
    for card in cards:
        if card["name"] == name:
            print("查询的结果：")
            display_one(card)
            delete_carde = update_carde(card)
            if delete_carde:
                cards.remove(card)
            break
    else:
        print("没查到要找的名片")


def update_carde(card):
    """
    更新修改名品
    @param card: 名片对象字典
    @return: 返回bool值
    """
    func_num = int(input("请选择功能：1/修改，2/删除 :"))
    if func_num == 1:
        card["name"] = input("修改名称：")
        card["mobile"] = input("修改电话：")
        card["qq"] = input("修改qq：")
        card["email"] = input("修改邮箱：")
        return False
    elif func_num == 2:
        return True
    else:
        print("功能选择错误！！")
        update_carde(card)


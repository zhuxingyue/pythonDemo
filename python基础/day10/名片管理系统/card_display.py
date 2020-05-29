def display_one(card):
    """
    显示单张名片
    @param card: 名片对象字典
    @return:
    """
    st = ["名称", "电话", "qq", "邮箱"]
    print("*********************************************************")
    for key in st:
        print(key.ljust(14), end="")
    print()
    show_card(card)
    print("*********************************************************")


def display_more(cards):
    """
    显示全部名品
    @param cards: 名片信息列表
    @return:
    """
    st = ["名称", "电话", "qq", "邮箱"]
    print("*********************************************************")
    for key in st:
        print(key.ljust(14), end="")
    print()

    for card in cards:
        show_card(card)
    print("*********************************************************")


def show_card(card):
    """
    名片字段显示排版
    @param card: 名片对象字典
    @return:
    """
    print(card["name"].ljust(15), end="")
    print(card["mobile"].ljust(15), end="")
    print(card["qq"].ljust(15), end="")
    print(card["email"].ljust(15))


# card({"name": "zhang", "mobile":"123", "qq":"123", "email":"213@"})

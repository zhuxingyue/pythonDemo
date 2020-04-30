from requestMethod import Method
from login import Login


class UpdateUser():

    # 更新用户信息
    url = "https://test2019.jiheapp.com/v1/user/info/base?"
    data = {
        "nickname": "蓝天白云2",
        "platform": "android",
        "token": "undq6gBCSmm5zs95"
    }

    data1 = {
        "avatar":  "/img/20200117u2atsumdn62b7dudpv6ttwm2vo03ejkf.jpg",
        "platform": "android",
        "version": "1.1.0",
        "token": data['token']
    }

    method = Method()

    # 初始化token
    def __init__(self, token):
        self.data['token'] = token
        self.data1['token'] = self.data['token']

    # 更新昵称
    def updateUserName(self, newName):
        self.data["nickname"] = newName
        return self.method.method("post", self.url, self.data)

    # 更新头像
    def updateUserHeadImage(self, imageAddress):
        self.data1['avatar'] = imageAddress
        return self.method.method("post", self.url, self.data1)


if __name__ == "__main__":
    # 更新昵称
    nickName = "测试1"

    # 更新头像
    image = "/img/20200116qlx0pf1pb76biekub3tcajfap22fxw6k.jpg"

    login = Login()
    re = login.login()
    token = re['data']['token']
    updateUser = UpdateUser(token)
    s = updateUser.updateUserName(nickName)
    s1 = updateUser.updateUserHeadImage(image)
    print(s)
    print(s1)

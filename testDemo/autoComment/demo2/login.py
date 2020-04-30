from requestMethod import Method


class Login():
    # 获取验证码
    url = "http://test2019.jiheapp.com//v1/user/auth/get_code?"

    # 登陆
    url1 = "http://test2019.jiheapp.com//v1/user/auth/login?"

    data = {
        "mobile": "15212340078"
    }

    data1 = {
        "mobile": data['mobile'],
        "code": "1234"
    }
    method = Method()

    def __init__(self, mobile="15212340078"):
        self.data['mobile'] = mobile
        self.data1['mobile'] = self.data['mobile']

    def getCode(self):
        return self.method.method("post", self.url, data=self.data)

    def login(self):
        self.getCode()
        re = self.method.method("post", self.url1, data=self.data1)
        return re['data']['token']


if __name__ == "__main__":
    login = Login()
    re = login.login()
    print(re)
    # print(re['data']['token'])

from login import Login
from requestMethod import Method


class Comment():
    # 用户评论
    url = "https://test2019.jiheapp.com/v1/user/course/add_reply?"

    # 评论数据
    data = {
        "course_id": "30",
        "parent": "0",
        "dialog": "0",
        "at_customer_id": "",
        "root": "0",
        "message": "好几回发过火几节课干活健康快乐",
        "platform": "android",
        "version": "1.1.0",
        "token": "RJkYD2pvMj6Up8nf"
    }

    method = Method()

    def __init__(self, course_id="30", token=None):
        self.data['token'] = token
        self.data['course_id'] = course_id

    def userComment(self, message=None):
        self.data['message'] = message
        return self.method.method("post", self.url, self.data)

    def userReplayCommet(self, course_id="30", id="0", message=None):
        self.data['course_id'] = course_id
        self.data['parent'] = id
        self.data['root'] = id
        self.data['message'] = message
        return self.method.method("post", self.url, self.data)


if __name__ == "__main__":
    # 提交评论
    message = "测试自动话脚本刷评论"

    # 用户回复评论
    message1 = "测试自动话脚本自动回复用户的评论"

    login = Login()
    re = login.login()
    token = re['data']['token']
    comment = Comment(token=token)
    s = comment.userComment(message)
    print(s)

    id = s['data']['id']
    s1 = comment.userReplayCommet(id, message1)
    print(s1)

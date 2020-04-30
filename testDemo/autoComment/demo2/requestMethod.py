import requests


class Method(object):

    def method(self, method="get", url=None, data=None):
        if method == "get":
            response = requests.get(url=url, params=data)
        else:
            response = requests.post(url=url, data=data)

        response = response.json()
        return response
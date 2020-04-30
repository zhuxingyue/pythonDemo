import requests
import upyun
from hashlib import md5
import base64
operations = {
    "server":"//v0.api.upyun.com/zxy-image-upyun",
    "operater":"operater123",
    "password":"UMO8vGxSTX5kX5v6eDNBztYIKLwznQ4e"
    "address":"zxy-image-upyun.test.upcdn.net"
}

url = "http://v0.api.upyun.com/zxy-image-upyun?"
data = {
    "authorization"="UPYUN <Operator>:<Signature>",
    "file"="file",
    "policy"="policy"
}
authorization = UPYUN <Operator>:<Signature><Signature> = Base64 (
    HMAC-SHA1 (
        <Password>,
        <post>&
        <URI>&
        <Date>&
        <Policy>&
        <Content-MD5>
    )
)

data1 = {
    "bucket": "zxy-image-upyun", 
    "save-key": r'/image/{year}/{mon}/{day}/{hour}_{min}_{sec}_{filename}{.suffix}', 
    "expiration": "1478674618", 
    "date": "Wed, 09 Nov 2016 14:26:58 GMT", 
    "content-md5": "7ac66c0f148de9519b8bd264312c4d64"
}
policy = Base64(data1)


import requests

def sendImg(img_path, img_name, img_type='image/jpeg'):
	"""
	:param img_path:图片的路径
	:param img_name:图片的名称
	:param img_type:图片的类型,这里写的是image/jpeg，也可以是png/jpg
	"""
	url = 'https://www.xxxxxxxxxx.com' # 自己想要请求的接口地址
	
	with open(img_path + img_name, "rb")as f_abs：# 以2进制方式打开图片
		body = {
			# 有些上传图片时可能会有其他字段,比如图片的时间什么的，这个根据自己的需要
			
			'camera_code': (None, "摄像头1"), 
			
			'image_face': (img_name, f_abs, img_type)
			# 图片的名称、图片的绝对路径、图片的类型（就是后缀）
			
			"time":(None, "2019-01-01 10:00:00")
			
			}
		# 上传图片的时候，不使用data和json，用files
		response = requests.post(url=url, files=body).json
		return response

  
if __name__=='__main__':
    # 上传图片
    res = sendImg(img_path, img_name)          # 调用sendImg方法
	print(res)

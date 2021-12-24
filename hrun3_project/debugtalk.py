import time
from utils.sign import sign_body


def int_to_str(arg):
    """int类型转字符串"""
    return str(arg)


def str_to_int(arg):
    """字符串转int类型"""
    return int(arg)


def register_user():
    """生成注册用户名称"""
    user = "test" + str(int(time.time()))
    time.sleep(1)
    return user


def goods_code():
    """随机生成商品编码goodscode"""
    # print(int(time.time()))
    time.sleep(0.1)
    goodscode = "sp_"+str(int(time.time()*100))
    return goodscode


def setup_request(request):
    """请求预处理，sign签名
    httprunner 3版本获取request请求参数是req_json"""
    print("request:", request)
    body = request.get("req_json")
    print('body:', body)  # {"username": x}
    sign = sign_body(body, apikey="12345678")
    print("sign: ", sign)
    # sign 加到请求body
    request["req_json"]["sign"] = sign
    print("新的request:", request)
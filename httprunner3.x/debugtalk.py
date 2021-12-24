import time
from utils.connect_mysql import DbConnect, dbinfo


def get_user():
    return [
        {"user": "test1"},
        {"user": "test2"},
        {"user": "test3"},
        {"user": "test4"},
    ]


def get_user_psw(n):
    account = []
    for i in range(1, n+1):
        account.append({"user": "test%s"%i, "psw": "123456"})
    return account


def register_user():
    user = "test" + str(int(time.time()))
    return user


def setup_hook():
    print("-----------setup-----------")


def teardown_hook():
    print("-----------teardown-----------")


def request_sign(request):
    body = request.get("req_json")
    print("body内容：", body)
    sign = "sign xxxxxxxxxxxxxxxxx"
    body["sign"] = sign
    request["req_json"] = body
    print("request 内容: ", request)


def response_status(response):
    print("status_code: ", response.status_code)
    response.status_code = 203
    print("修改后status_code: ", response.status_code)


import hashlib


def sign_body(body, apikey="12345678"):
    '''请求body sign签名'''
    # 列表生成式，生成key=value格式
    a = ["".join(i) for i in body.items() if i[1] and i[0] != "sign"]
    # print(a)
    # 参数名ASCII码从小到大排序
    strA = "".join(sorted(a))
    # print(strA)

    # 在strA后面拼接上apiKey得到striSignTemp字符串
    striSignTemp = strA+apikey

    # 将strSignTemp字符串转换为小写字符串后进行MD5运算

    # MD5加密
    def jiamimd5(src):
        m = hashlib.md5()
        m.update(src.encode('UTF-8'))
        return m.hexdigest()
    sign = jiamimd5(striSignTemp.lower())
    # print(sign)
    return sign


def login_sign(request):
    body = request.get("req_json")
    print("签名前body:", body)
    sign = sign_body(body=body, apikey="12345678")
    print("sign:", sign)
    request["req_json"]["sign"] = sign
    print("request:", request)


def get_db_goods(sp_id=1, key="goodsstatus"):
    db = DbConnect(dbinfo, database="apps")
    sql1 = 'SELECT * from apiapp_goods WHERE id = %s;' % sp_id
    res1 = db.select(sql1)
    print(res1)
    if len(res1) == 0:
        result = ''
    else:
        result = res1[0][key]
    return result


if __name__ == '__main__':
    print(get_user_psw(5))
    print(register_user())

    body = {
        "username": "test",
        "password": "123456"
    }
    r = sign_body(body=body, apikey="12345678")
    print(r)
    r = get_db_goods(sp_id=1, key="goodsname")
    print(r)

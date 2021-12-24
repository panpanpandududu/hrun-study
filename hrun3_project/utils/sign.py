import hashlib


def sign_body(body, apikey="12345678"):
    """请求body sign签名"""
    # 列表生成式，生成key=value格式
    a = ["".join(i) for i in body.items() if i[1] and i[0] != "sign"]
    # print(a)
    strA = "".join(sorted(a))   # 参数名ASCII码从小到大排序
    # print(strA)
    striSignTemp = strA+apikey   # 在strA后面拼接上apiKey得到striSignTemp字符串

    def jiamimd5(src):
        """MD5加密字符串"""
        m = hashlib.md5()
        m.update(src.encode('UTF-8'))
        return m.hexdigest()
    sign = jiamimd5(striSignTemp.lower())
    return sign
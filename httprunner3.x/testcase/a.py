
# import requests
#
# session = requests.Session()
#
# r1 = session.request(method="GET",
#                      url="https://www.cnblogs.com/yoyoketang",
#                      verify=False)
# print(r1.text)

# r1 = session.request(method="GET",
#                      url="http://49.235.92.12:8201/api/test/demo")
# print(r1.text)

#
# r2 = session.request(method="GET",
#                      url="http://49.235.92.12:8201/api/v1/goods",
#                      params={
#                          "page": 1,
#                          "size": 2
#                      })
# print(r2.text)
# url2 = "http://49.235.92.12:8201/api/v1/login"
# body = {
#     "username": "test",
#     "password": "123456"
# }
# r2 = session.request(method="POST",
#                      url=url2,
#                      json=body)
# print(r2.text)
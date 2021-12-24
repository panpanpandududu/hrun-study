import requests


url = "http://49.235.92.12:7005/api/v1/upfile/"


files = {"file": ["21.png", open("21.png", "rb"), "image/png"]}
body = {
    "title": "文件"
}
r = requests.post(url, files=files, data=body)
print(r.text)
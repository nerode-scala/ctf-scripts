import requests

with requests.session() as s:
    for i in range(0, 200):
        response = s.get("http://127.0.0.1/index.php?user=%s" % (str(i)))
        if "nerode" in response.text:
            print(response.url)

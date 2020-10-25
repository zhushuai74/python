import requests
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36 Edg/83.0.478.54'
}
response = requests.get('http://www.ofzhus.cn',headers)
print(response.text)
with open('boke','wb') as f:
        f.write(response.content)
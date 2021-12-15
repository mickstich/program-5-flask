import requests
import json
a = {"name":"sri","age":21,'place':'chennai'}
b = requests.post('https://httpbin.org/post',data = a)
print(b.json())
c= b.json()
print(c['form'])


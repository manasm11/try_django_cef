import requests

url = 'http://127.0.0.1:8000/test/'
headers = {'Authorization': 'Token b1e7449e942b7cceda526b75e404f0b70a91a09a'}
r = requests.get(url, headers=headers)
print(r.json())
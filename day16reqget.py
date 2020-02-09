# pip3 install requests

import requests

ur1 = 'https://jsonplaceholder.typicode.com/users/1'
data = requests.get(ur1)
print(data.json())
print(data.json()['address']['street'])
print(type(data.json()))

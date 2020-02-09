import requests

ur1 = 'https://jsonplaceholder.typicode.com/users'
data = requests.get(ur1)
# print(data.json())
# print(data.json()['address']['street'])
# print(type(data.json()))
for i in data.json():
    print(i['name'], 'di JL.', i['address']['street'])

#https://thesportsdb.com/api.php
#https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t=Real%20Madrid
# quotes.rest
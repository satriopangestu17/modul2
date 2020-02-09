#APIs up to 1000 cals day. artinya 1 internet misal purwadhika1 cuma bisa 1000.
#2e8f558a2447b345cfeede733d4b3982 API key
#response class (status 200) artinya oke

#di postman untuk memasukkan API di authorization
#atau di headers masukin API key

import requests

host = 'https://developers.zomato.com/api/v2.1' ##URL categories
kategori = '/categories'
apikey = '2e8f558a2447b345cfeede733d4b3982'
headInfo = {'user-key': apikey}  ##use-key adalah parameters di developers.zomato.com/api
url = host +  kategori
data = requests.get(url, headers=headInfo) ##headers harus berbentuk dictionary

print(data.json())
# print(data.json()['categories'])
# print(data.json()['categories'][0]['categories']['id'])

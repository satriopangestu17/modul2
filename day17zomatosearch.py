#di postman untuk memasukkan API di authorization
#atau di headers masukin API key
import requests

kota = input('nama kota: ')
url1 = f'https://developers.zomato.com/api/v2.1/cities?q={kota}'
apikey = '2e8f558a2447b345cfeede733d4b3982'
headinfo = {'user-key': apikey}
data1 = requests.get(url1, headers=headinfo)
idkota = int(data1.json()['location_suggestions'][0]['id'])
print(idkota)
# print(data1)

# makanan = input('nama makanan: ')
# url2 = f'https://developers.zomato.com/api/v2.1/search?entity_id={idkota}&entity_type=city&q={makanan}'
# apikey = '2e8f558a2447b345cfeede733d4b3982'
# headinfo = {'user-key': apikey}
# data2 = requests.get(url2, headers=headinfo)
# idsearch = data2.json()['restaurants'] 
# print (len(idsearch))

# for i in range(len(idsearch)):
#     namarestoran = idsearch[i]['restaurant']['name']
#     lokasirestoran = idsearch [i]['restaurant']['location']['address']
#     print(f'{namarestoran}, Lokasi: {lokasirestoran}')

# x = 'abc'
# for i in range (len(x)):
#     z = x[i]
#     print(z)
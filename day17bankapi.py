import requests
listbank = ['bca', 'bi', 'bjb', 'bni', 'bri', 'btn', 'bukopin',
'cimb', 'commonwealth', 'danamon', 'hsbc', 'jtrust', 'mandiri', 'mayapada', 
'maybank', 'mega', 'muamalat', 'ocbc', 'panin', 'permata', 'panin', 'permata', 
'sinarmas', 'uob', 'woorisaudara']

# if bank in listbank:
#     url = f'https://kurs.web.id/api/v1/{bank}'
#     data = requests.get(url)
# elif bank == 'blockchain':
#     ur1 = 'https://blockchain.info/ticker'
#     datablock = requests.get(ur1)
# urb = f'https://kurs.web.id/api/v1/'
# databank = requests.get(urb)
# daftarbank = databank.json()['bank']
# print (daftarbank)

# inputnominal = int(input('input USDorIDR: '))
# nominal1 = int(data.json()['jual'])
# print(nominal1)
# usdtorp = inputnominal * nominal1
# hasilusdtorp = f'nilai USD {nominal1} adalah IDR {usdtorp}'
# print(hasilusdtorp)

# inputnominal = int(input('input USDorIDR: '))
# nominal2 = int(data.json()['beli'])
# print(nominal1)
# rptousd = inputnominal * nominal2
# hasilrptousd = f'nilai IDR {nominal2} adalah USD {usdtorp}'
# print(hasilrptousd)

# x = 1 => idr to usd
# x = 2 => usd to idr
# x = 3 => usd to crypto
# x = int(input('masukkan pilihan konversi: '))
bank = input('ketik nama bank: ')
if bank not in listbank or not 'bitcoin':
    print('maaf bank tidak ada')   ##kenapa ini tidak keprint?

elif bank in listbank:
    x = int(input('masukkan pilihan konversi: '))
    url = f'https://kurs.web.id/api/v1/{bank}'
    data = requests.get(url)
    if x == 1:
        # url = f'https://kurs.web.id/api/v1/{bank}'
        # data = requests.get(url)
        inputnominal1 = int(input('input USDorIDR: '))
        nominal1 = int(data.json()['jual'])
        print(nominal1)
        usdtorp = inputnominal1 / nominal1
        hasilusdtorp = f'nilai IDR {inputnominal1} adalah USD {usdtorp}'
        print(hasilusdtorp)
    elif x == 2:
        # url = f'https://kurs.web.id/api/v1/{bank}'
        # data = requests.get(url)
        inputnominal2 = int(input('input USDorIDR: '))
        nominal2 = int(data.json()['beli'])
        print(nominal2)
        rptousd = inputnominal2 * nominal2
        hasilrptousd = f'nilai USD {inputnominal2} adalah IDR {rptousd}'
        print(hasilrptousd)

elif bank == 'bitcoin':  
    x = int(input('masukkan pilihan konversi: '))
    if x == 3:
        ur1 = 'https://blockchain.info/ticker'
        datablock = requests.get(ur1)
        inputnominal3 = int(input('input : '))
        nominal3 = int(datablock.json()['USD']['sell'])
        print(nominal3)
        usdtobit = inputnominal3 / nominal3
        hasilusdtobit = f'nilai USD {inputnominal3} adalah bit {usdtobit}'
        print(hasilusdtobit)
else:
    print('maaf bank tidak ada')





#idr to usd
#usd to idr
#usd to bitcoin


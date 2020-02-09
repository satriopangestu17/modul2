import requests
listbank = ['bca', 'bi', 'bjb', 'bni', 'bri', 'btn', 'bukopin',
'cimb', 'commonwealth', 'danamon', 'hsbc', 'jtrust', 'mandiri', 'mayapada', 
'maybank', 'mega', 'muamalat', 'ocbc', 'panin', 'permata', 'panin', 'permata', 
'sinarmas', 'uob', 'woorisaudara']



bank = input('ketik nama bank: ')
if bank not in listbank and not 'bitcoin':
    print('maaf bank tidak ada')

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
    x = 3
    if x == 3:
        ur1 = 'https://blockchain.info/ticker'
        datablock = requests.get(ur1)
        inputnominal3 = int(input('input : '))
        nominal3 = int(datablock.json()['USD']['sell'])
        print(nominal3)
        usdtobit = inputnominal3 / nominal3
        hasilusdtobit = f'nilai USD {inputnominal3} adalah bit {usdtobit}'
        print(hasilusdtobit)





#idr to usd
#usd to idr
#usd to bitcoin


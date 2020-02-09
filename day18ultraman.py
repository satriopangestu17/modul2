from bs4 import BeautifulSoup
import requests

web = requests.get('http://www.scifijapan.com/articles/2015/10/04/bandai-ultraman-ultra-500-figure-list/')
data = BeautifulSoup(web.content, 'html.parser')
# ultra = data.strong
strong = data.find_all('strong')
output = []
for i in strong:
    output.append(i.text)
print(output)
ultra = output[2:36] ##di cek dulu ada di urutan ke berapa
monster = output[37:110]  ##di cek dulu ada di urutan ke berapa
print(ultra)
print(monster)


# for i in ultra.find_all('strong'):
#     print(i.text)

#digimon. image scr

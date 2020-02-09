# #postman to see inside the http clearly
# import requests

# klub = input('ketik nama klub ')
# ur2 = f'https://www.thesportsdb.com/api/v1/json/1/searchplayers.php?t={klub}'
# data = requests.get(ur2)
# players = data.json()['player']
# # print(data.json())

# # player = variable
# for player in players:
#     print(f"{player['strPlayer']} ({player['strPosition']})") 


#manchester united = man united

# b = {[{'strTeam':'Arsenal', 'strPlayer':'Hector'}]}

# print(b)

#zip
a = ['nama', 'usia', 'negara']
b = ['radi', '22', 'indonesia']
kombi = dict(zip(a, b))
print(kombi)


##for draw and break
x= 3
y= 4
for row in range(7,6,-1):  ## 5-4=1 .jadi akan membetuk  1 matriks, dengan angka dimulai dari 1 
    for column in range(4,1,-1): #GUNA UNTUK MEMBENTUK POLA GAMBARNYA
        print(x, y, row+1) ##untuk isi gambarnyaa
        row += 1
        x += 1 
        y -=1
        column += 1  ##column ditambah ga akan ngaruh , misal dimasukkan ke print
    print()
    # break

x= 3
y= 4
z= 10
for row in range(6,7,1):  ## 5-4=1 .jadi akan membetuk  1 matriks, dengan angka dimulai dari 1 
    for column in range(1,4,1): #GUNA UNTUK MEMBENTUK POLA GAMBARNYA
        print(x, y, z) ##untuk isi gambarnyaa
        # row += 1
        x += 1 
        y +=1
        z += 1
        column += 1  ##column ditambah ga akan ngaruh , misal dimasukkan ke print
    # print()
    # break
   
    

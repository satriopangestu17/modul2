import xlrd
import xlsxwriter
excel = input("Masukkan nama file excel : ")
asal = input("Masukkan nama sheet dasar yang akan diupdate datanya : ")
tujuan = input("Masukkan nama sheet baru untuk update : ")
file = xlrd.open_workbook(excel)
sheet = file.sheet_by_name(asal)
data = []
for i in range(sheet.nrows):
    data.append(sheet.row_values(i))

newfile = xlsxwriter.Workbook(excel)
sheet1 = newfile.add_worksheet(asal)
newsheet = newfile.add_worksheet(tujuan)
for i in range(len(data)):
    for j in range (len(data[0])):
        sheet1.write(i, j, data[i][j])
for i in range(len(data)):
    for j in range (len(data[0])):
        newsheet.write(i, j, data[i][j])
def dataBaru():
    noUrut = len(data)
    ask = input("Apakah anda ingin menambahkan data (Y/N) : ")
    while ask == ("Y"):
        A = input("Masukkan nama : ")
        B = input("Masukkan kota : ")
        C = [(noUrut), A, B]
        for j in range (len(data[0])):
            newsheet.write(noUrut,j,C[j])
        noUrut += 1
        ask = input("Apakah anda ingin menambahkan data (Y/N) : ")
        if ask == ("N"):
            break

dataBaru()
newfile.close()



# API = manggil backend from database dari frontend(tampilan depan)
#http, ftp(file transfer protocol)masukin data ke facebook. Sending Mail Protocol(contoh:subrscribe)

## mobile/laptop <=>API<=> e(backend server <=> connect database)
#http://jsonplaceholder.typicode.com/users
#protokol http, get=untuk backend nya ngasih data yang kita minta.
#postman
## get 
# view-source
#view-source:https://www.tokopedia.com/?c=676207368&ds_rl=1261170&gclid=CjwKCAiA8K7uBRBBEiwACOm4d45iNA3i25VAl01ctSoN_9lc2Ab-RdDTgFX756oToktMMC-4w2G59BoCty8QAvD_BwE&gclsrc=aw.ds

#python GET request => API
# urllib
# request
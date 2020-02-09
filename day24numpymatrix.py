import numpy as np
# x = [1,2,3,4,5]
# y = np.array(x)  #digunakan apabila ada operasi2 matrix

# # print(x[::2])
# # print(y[::2])
# print(x + x)
# print(y + y)  #seperti penjumlahan matrix

# x = (1,2,3)
# y = np.array(x)  #digunakan apabila ada operasi2 matrix
# print(x)
# print(y)
# print(type(y))

# z = [1 2 3]  #salah
# print(z)

# x = [[1,2,3], [4,5,6]]
# y = np.array(x)

# # print(x[1,1]) #yang ini ga bisa #error
# print(x[1][1])
# print(y[1,1])

x = [1,2,3]
x = np.array (x)
y = [[1,2,3], [4,5,6]]
y = np.array (y)
z = [[[1,2,3], [4,5,6], [7,8,9]]] #kalau isi tiap list ga sama banyak ga keitung dimensi
z = np.array (z)
print(x)
print(x.ndim)  #penting untuk tau matrix berapa dimensi.
print(x.size)  
print(y)
print(y.ndim)
print(y.size)
print(z)
print(z.ndim) #untuk tau matrix berapa dimensi. ada lis1 list2 list3
print(z.size)
print(z.dtype) #int32 digit:10,4byte. int 64 digit:20,8byte
print(z.itemsize) #byte nya

z = z.astype('float64') #ngubah jadi float
print(z)
print(z.dtype)
print(z.ndim)
print(z.shape)

# a = np.array([1])
# print(a.ndim)
# print(a.shape)

# # a = np.array([1,2,3]) #selain bikin list seperti dikiri biasa bisa bikin pake range seperti dibawah:
# # print(np.arange(1, 10, 2))
# # print(list(range(10, 1, -1)))

# print(np.random.random(10)) #random 10 elemen, nilainya antara 0 sampe 1
# print(np.random.rand(2,4)) #random 2 dimensi, isinya 4 elemen
# print(np.random.randint(7)) #random integer nilai maksimal 7
# print(np.random.randint(7, size=(2,5))) #random integer nilai maksimal 7, ada 10 elemen

#spacing
print(np.linspace(1, 10, 9)) # dari1 sampe 5, ada 5 elemen
print(np.linspace(1, 100, 5)) # angka dari1 sampe100, ada 5 elemen

# a = [(1,2,3), (4,5,6), (7,8,9)]
# a = np.array(a)
# print(a)
# print(a.ndim)
# print(a[0,2]) # a[0][2]
# print(a[0:2, 0:2]) 
# print(a[0:, 2]) 
# print(a[0:3, 0:2]) #dimensi pertamanya mau keluarin apa, lalu dimensi keduanya mau keluarin
# print(a[0:, 0:1]) #keluarnya 2 list, 2 dimensi
# print(a[0:3, 0]) #keluarnya 1 list. satu dimensi.

# #print(a[0,2])  #a[0][2]
# print(a[0:, [0,2]])
# #print(a[0:, 1])
# print(a[0:, [0,-1]])
# print(a[0:, :1]) #size = 3 shape=(3,1) ##size nya sama shape nya beda
# print(a[0:, 0])   #size=3 shape=(3,) = [1,4,7]
# print(a[0:, :1].shape)
# print(a[0:, :1].reshape(3,)) #untuk mengubah harus konsisten dengan jumlah sizenya. hasil sama dengan print(a[0:, 0])
# print(a[0:, 0].shape)
# print(a[0:, 0].reshape(1,3,1)) # ada 3 dimensi, dimensi pertama ada1 elemen, dimensi2 ada3 elemen,hasil sama dengan print(a[0:, :1])
# print(a[0:, 0].reshape(3,1,1)) # ada 3 dimensi, dimensi pertama ada1 elemen, dimensi2 ada3 elemen, 
# print(a[0:, :1].size)
# print(a[0:, 0].size)

# A = |0 -7|       B = |2 4|
#     |-1 3|           |3 8|

# a = np.array([[0,-7],[-1,3]])
# b = np.array([[2,4],[3,8]])
# print(a)
# print(b)
# print(a+b) #operasi penjumlahan matrix
# print(a-b) #operasi pengurangan matrix
# print(a+2) #tiap elemen ditambah 2

x = np.array([1,2,3,4])
print(x + x)
print(x - x)
print(x + 3)
print(x - 3)
print(x * 3)
print(x / 3)
x[0] += 2  ##yang elemen 0 saja yang ditambah
print(x)

#SOAL
# 2x +1y = 5
# 1x +1y = 7
#spldv
# |2 1| | x | = | 5 |
# |1 1| | y |   | 7 |

a = np.array([[2,1], [1,1]])
b = np.array([5, 7])
hasil = np.linalg.solve(a, b) #linalg.linearaljabar
print(hasil)

#soal:  3x = 6  x=>2
# |3| |x| = |6|
# x = np.array([3]).reshape(1,1) atau bisa x nya seperti dibawah
x = np.array([[3]])
y = np.array([6])
z = np.linalg.solve(x, y)
print(z)
print(x[0:, :2].shape)
# print(y[0:, :1].shape)


# soal: berapa 2e - 3r=?
q = np.array([[4,7], [3,2]])
w = np.array([2, -5])
value = np.linalg.solve(q, w)
print(value)
value1 = value[0]
value2 = value[1]
print(value1)
print(value2)

e = np.array(value1)
r = np.array(value2)
print(2*e - 3*r)

#a + k =25 .   2a + 4k =70. ada berapa ayam dan berapa kambing?
j = np.array([[1,1], [2,4]])
k = np.array([25, 70])
nilai = np.linalg.solve(j, k)
print(nilai)
nilai1 = nilai[0]
nilai2 = nilai[1]
print(f'ayam ada {nilai1}')
print(f'kambing ada {nilai2}')
# o = np.array(nilai1)
# p = np.array(nilai2)
# print()



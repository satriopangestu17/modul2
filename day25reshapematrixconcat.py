import numpy as np

x = [[1,20,3,400,5],[3,5,7,9,11]]
y = np.array(x)
z = np.array ([1,2,3,5,6,8,9,11,12,13,14,10])

print(y)
print(y.shape)
print(y.max())
print(y.reshape(-1))  #jadi 1 dimensi ketik (-1, .. , ..) ga mesti jadi 1 dimensi tapi jadi terserah
# y = np.reshape(y,(10,1))  #jadi 2 dimensi
print(y.shape)
print(y)
# print(z)
# z = np.reshape(z, (1, 1, 12))  ## untuk mengubah jadi 3 dimensi ketik (1, .., ..)
# print(z) 
# z = np.reshape(z, (1, 12))  ## untuk mengubah jadi 2 dimensi ketik (.., ..)
# print(z) 
# print(np.argmax(z)) #max array di index ke berapa berdasar column
# z = np.reshape(z, (12))  ## untuk mengubah jadi 1 dimensi ketik ( ..) 
# print(z)
print(y.reshape(1, 5, 2)) #ubah jadi 3 dimensi dari 2 dimensi, ada 2 komponen di tiap [], ada 5 []
print(y.reshape(1, 10, 1)) #ubah jadi 3 dimensi dari 2 dimensi, ada 1 komponen di tiap [], ada 10 []
print(y.reshape(2,-1))  ## bentuk sama tidak berubah
print(y.reshape(5,2))  ## 2 dimensi, ada 5 [], isinya ada 2 komponen
# print(y.min())
# print(np.argmax(y)) #untuk mengetahui di indeks keberapa max array
# print(np.argmax(y, axis=0)) #max array
# # print(np.argmin(y))

# # a = np.array([[1,2,3],[4,5,6]])
# # b = np.array([[0,0,0],[0,0,0]])
# # print(b)
# # print(b.dtype)

# # c = np.zeros((2,3), dtype='int64') #mengubah float jadi int
# # print(c)
# # print(c.dtype)

# # d = np.ones((3,3))  ##np.ones isinya 1 semua
# # print(d)

# # a = np.array([[1,2,3],[1,2,3], [1,2,3]])
# # d = np.ones((3,3))
# # print(a * d)

# # x = 1  #jadi 1 bisa dikatakan true. 0 adalah false
# # if x:   
# #     print(x)
# # else:
# #     print(x)

# # x = np.zeros((3,3), dtype=bool)
# # print(x)

# # x = np.ones((3,3), dtype=bool)
# # print(x)

# # lain = np.full((3,3), True, dtype=bool)
# # print(lain)

# # lain = np.full((3,3), 1)  ##full bisamkeluar apa aja
# # print(lain)


# # lain = np.full((3,3), 'Andi')  ##full bisamkeluar apa aja
# # print(lain)

# # # lain = np.full((1,3), 'Andi')  ##full bisamkeluar apa aja
# # # print(lain)
# # print(type(lain))
# # print(lain.tolist())
# # print(type(lain.tolist()))

# # lain = lain.tolist()
# # print(lain)
# # print(type(lain))





# x = [0,1,2,3,4]
# y = [5,6,7,8,9]
# # # buat list z = [[0,1,2,3,4], [5,6,7,8,9]]

# # #cara 1
# # z = []
# # z.append(x)
# # z.append(y)
# # print(z)

# # #cara 2 
# # z = [x, y]
# # print(z)

# # #cara 3
# # z = np.array(x+y).reshape(2,-1).tolist()
# # print(z)

# # #cara 4
# # a = []
# # a.extend(x)
# # a.extend(y)
# # z = np.array(a).reshape(2,-1).tolist()
# # print(a)

# # #cara 5
# # xnp = np.array(x)
# # ynp = np.array(y)
# # z =np.concatenate([[xnp], [ynp]], axis=0) ## axis semakin besar dimensi semakin kecil
# # print(z)

# # a = np.concatenate([xnp,ynp])
# # print(a)

# # # a = np.concatenate([xnp,ynp], axis=1) # gabisa axis kalo 1 dimensi
# # # print(a)

# # #cara 6
# # z = np.vstack([xnp, ynp])
# # print(z)
# # listz = z.tolist()
# # print(listz)

# # # cara 7
# # z = np.r_[[xnp], [ynp]].tolist()
# # print(z)

# # # cara 8
# # z = np.row_stack((xnp, ynp)).tolist()
# # print(z)

# # #cara 9
# a = np.arange(5)
# b = np.array([5,6,7,8,9])
# c = np.vstack([a,b])  #vertical stack ## seperti biasa (2, 5)
# print(c)
# c =np.hstack([a,b])  #horizontal stack ## jadi (1, 10)
# print(c)
# import numpy as np

# x = [[1,20,3,400,5],[3,5,7,9,11]]
# y = np.array(x)
# z = np.array ([1,2,3,5,6,8,9,11,12,13,14,10])

# print(y)
# print(y.shape)
# print(y.max())
# print(y.reshape(-1))  #jadi 1 dimensi ketik (-1, .. , ..)
# # y = np.reshape(y,(10,1))  #jadi 2 dimensi
# print(y.shape)
# print(y)
# # print(z)
# # z = np.reshape(z, (1, 1, 12))  ## untuk mengubah jadi 3 dimensi ketik (1, .., ..)
# # print(z) 
# # z = np.reshape(z, (1, 12))  ## untuk mengubah jadi 2 dimensi ketik (.., ..)
# # print(z) 
# # print(np.argmax(z)) #max array di index ke berapa berdasar column
# # z = np.reshape(z, (12))  ## untuk mengubah jadi 1 dimensi ketik ( ..) 
# # print(z)
# # print(y.reshape(1, 10, 1)) #ubah jadi 3 dimensi
# # print(y.reshape(2,-1))
# # print(y.min())
# print(np.argmax(y)) #untuk mengetahui di indeks keberapa max array
# print(np.argmax(y, axis=0)) #max array
# # print(np.argmin(y))

# # a = np.array([[1,2,3],[4,5,6]])
# # b = np.array([[0,0,0],[0,0,0]])
# # print(b)
# # print(b.dtype)

# # c = np.zeros((2,3), dtype='int64') #mengubah float jadi int
# # print(c)
# # print(c.dtype)

# # d = np.ones((3,3))  ##np.ones isinya 1 semua
# # print(d)

# # a = np.array([[1,2,3],[1,2,3], [1,2,3]])
# # d = np.ones((3,3))
# # print(a * d)

# # x = 1  #jadi 1 bisa dikatakan true. 0 adalah false
# # if x:   
# #     print(x)
# # else:
# #     print(x)

# # x = np.zeros((3,3), dtype=bool)
# # print(x)

# # x = np.ones((3,3), dtype=bool)
# # print(x)

# # lain = np.full((3,3), True, dtype=bool)
# # print(lain)

# # lain = np.full((3,3), 1)  ##full bisamkeluar apa aja
# # print(lain)


# # lain = np.full((3,3), 'Andi')  ##full bisamkeluar apa aja
# # print(lain)

# # # lain = np.full((1,3), 'Andi')  ##full bisamkeluar apa aja
# # # print(lain)
# # print(type(lain))
# # print(lain.tolist())
# # print(type(lain.tolist()))

# # lain = lain.tolist()
# # print(lain)
# # print(type(lain))





# x = [0,1,2,3,4]
# y = [5,6,7,8,9]
# # # buat list z = [[0,1,2,3,4], [5,6,7,8,9]]

# # #cara 1
# # z = []
# # z.append(x)
# # z.append(y)
# # print(z)

# # #cara 2 
# # z = [x, y]
# # print(z)

# # #cara 3
# # z = np.array(x+y).reshape(2,-1).tolist()
# # print(z)

# # #cara 4
# # a = []
# # a.extend(x)
# # a.extend(y)
# # z = np.array(a).reshape(2,-1).tolist()
# # print(a)

# # #cara 5
# # xnp = np.array(x)
# # ynp = np.array(y)
# # z =np.concatenate([[xnp], [ynp]], axis=0) ## axis semakin besar dimensi semakin kecil
# # print(z)

# # a = np.concatenate([xnp,ynp])
# # print(a)

# # # a = np.concatenate([xnp,ynp], axis=1) # gabisa axis kalo 1 dimensi
# # # print(a)

# # #cara 6
# # z = np.vstack([xnp, ynp])
# # print(z)
# # listz = z.tolist()
# # print(listz)

# # # cara 7
# # z = np.r_[[xnp], [ynp]].tolist()
# # print(z)

# # # cara 8
# # z = np.row_stack((xnp, ynp)).tolist()
# # print(z)

# # #cara 9
# a = np.arange(5)
# b = np.array([5,6,7,8,9])
# c = np.vstack([a,b])  #vertical stack ## seperti biasa (2, 5)
# print(c)
# c =np.hstack([a,b])  #horizontal stack ## jadi (1, 10)
# print(c)

# # a = np.arange(6).reshape(2, -1)
# # b = np.array([5,6,7,8,9,10]).reshape(2, -1)
# # c = np.vstack([a,b])  #vertical stack
# # print(c) # yang 2 diatas yang a, 2 yang dibawah yang b
# # c =np.hstack([a,b])
# # print(c) #jadi 2 rows

# c = np.vstack([a,b])
# d = np.concatenate([a,b], axis=0) ##hasil akan sama dengan h stack
# e = np.row_stack((a,b))
# f = np.r_[a, b]
# print(c)
# print(d)
# print(e)
# print(f)
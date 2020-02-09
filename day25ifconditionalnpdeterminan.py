import numpy as np

z = np.arange(1, 11)
print(z)
print(z[1::2])
print(z[z%2 == 0]) ## nump py bisa pake conditional if

z[z % 2 != 0] = 0  #ngubah ganjil jadi 0
print(z)

#hasil akan sama :
# print(np.where(z % 2!=0,0,z))

x = np.arange(10,20)
print(x[np.where(x<16)])
print(np.where(x<16))  ##menunjukkan posisi index nya

##berikut hasilnya akan sama:
# print(x[np.where((x>14) & (x<18))])
# print(x[(x>14) & (x<18)])
# print(x[np.where(np.logical_and(x>14,x<18))])
# print(x[5:8])


#cari determinan mat 2 x 2
x = np.array([[3,1], [2, 5]])
print(x)
print(np.linalg.det(x)) ##Determinan

# matrix 3 x 3
y = np.array([[1,2,1],[3,3,1],[2,1,2]])
print(y)
print(np.linalg.det(y))

#invers matrix.= 1/determinan x (dibalik). Z x Zinverse = I
z = np.array([[3,2], [1,4]])
print(z)
print(np.linalg.inv(z))
print(z@np.linalg.inv(z)) #untuk jadiin matrix indentitas
#dot product
print(z.dot(np.linalg.inv(z)))

# #cross product
# print(np.cross(z,z))

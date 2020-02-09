import numpy as np


# array = np.arange(12).reshape(4, 3) 
array = np.array([[1,10,3],[12,15,6]])
print("INPUT ARRAY : \n", array) 

# No axis mentioned, so works on entire array 
print("\nMax element : ", np.argmax(array)) ## indeks untuk angka yg memiliki nilai max dari keseluruhan, dihitung dari 0 berdasr column
print("\nIndices of Max element : ", np.argmax(array, axis=0)) #untuk mengetahui di indeks keberapa max array. dihitungnya berdasar column
# print("\nIndices of Max element : ", np.argmax(array, axis=1)) #array with dimension of 2

# print("\nIndices of Max element : ", np.argmin(array, axis=1)) #array with dimension of 2
# print(np.where(array[1],))  ##true=1

# a is an array of integers. 
a = np.array([[1, 2, 3], [4, 5, 6]]) 
  
print(a) 
  
print ('Indices of elements <4') 
  
b = np.where(a<4) 
print(b) 
  
print("Elements which are <4") 
print(a[b])
print(a[0][1])

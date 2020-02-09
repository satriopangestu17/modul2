x = [3,32,89,1,120]
sortir = []
i = 0
minX = x[0]
while len(x) > 0:
    if x[i] <= minX:
        minX = x[i]
    i += 1
    if i == len(x):
        sortir.append(minX)
        x.remove(minX)
        if x:
            minX = x[0]
        i = 0
print(sortir)
    

import numpy as np
#swap

x = np.arange(1, 10).reshape(3, -1)
print(x) #bentuk awal

print(x[:, [1,0,2]]) # ngatur row or dimensi
print(x[:, [0,0,0]]) #munculin semua dimensi pertama atau row pertama

print(x[[1,0,2], :]) 

#transpose
# a b
# c d  =  a c e
# d e     b d f

a = np.array([[1,2], [3,4], [5,6]])
print(a)
print(a.transpose())
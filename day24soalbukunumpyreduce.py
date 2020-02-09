# 2bu + pe + ph =4700
# bu + 2pe + ph =4300
# 3bu + 2pe + ph =7100
import numpy as np

x = np.array([[2,1,1], [1,2,1], [3,2,1]])
y = np.array([4700, 4300, 7100])
nilai = np.linalg.solve(x, y)
print(nilai)
print(nilai.dtype)
nilaibuku = nilai[0]
print(nilaibuku)
nilaipe = nilai[1]
print(round(nilaipe))
nilaiph = nilai[2]
print(nilaiph)

# x = [1,2,3,4,5]
# y = np.array(x)
# print(max(x))
# print(min(x))
# print(y.max())
# print(y.min())
# print(y.sum())

from functools import reduce
x = [1,2,3,4,5]
xsum = reduce(lambda a,b: a+b, x)  ##a,b berpasang pasangan, a+b tiap pasangan ditambah, variabel x
print(xsum)  ##sum

## cara cari nilai maksimal without library np
xmax = reduce(lambda a,b: a if (a>b) else b, x)
print(xmax)


xmin = reduce(lambda a,b: a if (a<b) else b, x)
print(xmin)

y = np.array(x)
print(np.mean(y))
print(np.median(y))
print(np.pi)
print(np.sin(0))
print(np.cos(0))





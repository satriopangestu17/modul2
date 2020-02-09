import pandas as pd 
import numpy as np

# x = [9,2,5,3,4,5,7,4,3,5,7]
# y = pd.Series(np.array(x))
# print(y)
# print(y[2]) ##manggil berdasar index sebelah kiri

# x = ['Andi', 'Budi', 'Caca']
# y = pd.Series(np.array(x))
# print(y)
# print(y[2]) ##manggil berdasar index sebelah kiri
# print(y[0::2]) 

# x = [9,2,5,3,4]
# y = pd.Series(np.array(x), index = ['a', 'b', 'c', 'd', 'e'], name = 'Test') ##index dikirinya kadi a,b,c,d,e
# print(y)
# print(y[2]) ##manggil berdasar index sebelah kiri
# print(y[0::2]) 

# # pandas.core.series.Series ##bkl muncul type nya ini
# print(y['b'])

# x = [9,2,5,3,4]
# y = pd.Series( data = {'a': 2, 'b' : 3}
# , name = 'Test') ##index dikirinya kadi a,b,c,d,e
# print(y)

##DATAFRAME
# x = [2,4,6,8,10]
# df = pd.DataFrame(x) #nama kolom 0
# print(df) 

# x = [2,4,6,8,10]
# df = pd.DataFrame(x, columns=['Nilai']) #nama kolom 0
# print(df) 
# print(type(df))
# print(df.shape) ##jumlah baris berapa kolomnya berapa
# baris, kolom = df.shape
# print(kolom)
# print(baris)

x = [[1,2], [3,4], [5,6], [7,8]]
df = pd.DataFrame(x)
print(df)

# x = [2,4,6,8,10]
# y = [1,3,5,7,9]
# df = pd.DataFrame([x,y]) 
# print(df) 
# baris, kolom = df.shape
# print(kolom)

# #mengubah jadi 2 kolom.
# x = [2,4,6,8,10]
# y = [1,3,5,7,9]
# z = (map(lambda a, b: [a, b], x, y))
# z = list(z)
# print(z)
# df = pd.DataFrame(z) 
# print(df) 
# baris, kolom = df.shape
# print(kolom)
# print(df[0])
## ada jadi ada namanya
# df = pd.DataFrame()
# df['X'] = x
# df['Y'] = y
# print(df)

# x = [2,4,6,8,10]
# y = [1,3,5,7,9]
# z = 'david'

# df = pd.DataFrame()
# df['X'] = x
# df['Y'] = y
# df['Z'] = z
# print(df)

# x = [2,4,6,8,10]
# y = [1,3,5,7,9]
# z = list('david')

# ## df = pd.DataFrame([x,y,z])
# df = pd.DataFrame()
# df['X'] = x
# df['Y'] = y
# df['Z'] = z
# print(df)

x = [2,4,6,8,10]
y = [1,3,5,7,9]
z = 'david'

df = pd.DataFrame([x,y,list(z)])

print(df)







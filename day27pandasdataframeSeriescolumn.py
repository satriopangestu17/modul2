# pip3 install pandas
# import pandas 
import pandas as pd  ##untuk singkat
import numpy as np

x = np.array([1,2,3,4,5,6,7,8,9])
print(x)
xSeries = pd.Series(x)  #bentuk jd seperti tabel dengan 1 kolom
print(xSeries)

xDataFrame = pd.DataFrame([[1,2], [3,4], [4,5]], columns=['A', 'B'], index=[1,3,2])
# xDataFrame = pd.DataFrame([[1,2], [3,4], [4,5]], columns=['A', 'B'], index=range(1,4))
print(xDataFrame)  ##nampilin keseluruhan
# kolom beserta datanya adalah series

# xDataFrame = pd.DataFrame([[1,2], [3,4], [4,5]], columns=['A', 'B'])
# print(xDataFrame.head(1))
# print(xDataFrame.tail(1))
# print(xDataFrame['A'])

# b = ['a':'1','c':'2','d':'3','e':'4']
# b= dictionary(b)
# print

hari = {'senin':'monday', 'selasa':'tuesday'}
print(list(hari.values()))
print(list(hari))

print((((1.5/3)*(2/3))/((1.5/3)+(2/3)))*2)
import pandas as pd 
import numpy as np

# data = [['Andi', 'Jakarta', 'PNS'],
# ['Andi', 'Jakarta', 'Karyawan Swasta'],
# ['Caca', 'Jakarta', 'Ibu Rumah Tangga'],
# ]

# dfData = pd.DataFrame(data,
# index = list('xyz'),
# columns = ['Nama', 
# 'Kota', 'Pekerjaan'])
# print(dfData)

data = { 
    'x': [123,321,213],
    'y': [234,432,324],
    'z': [345,543,435]
}
df = pd.DataFrame(data, index=[1,2,3])
print(df)

# data = [
#     {'nama': 'Andi', 'kota':'Jakarta'},
#     {'nama': 'Andi', 'kota':'Jakarta'},
#     {'nama': 'Andi', 'kota':'Jakarta'},
#     {'nama': 'Andi', 'kota':'Jakarta', 'job':'PNS'},
#     ]
# df = pd.DataFrame(data)
# print(df)
# #Nan not a number

data = [
    {'nama': 'Andi', 'kota':'Jakarta'},
    {'nama': 'Andi', 'kota':'Jakarta', 'job': np.zeros},
    {'nama': 'Andi', 'kota':'Jakarta', 'job':'NaN'},  ##bukan NaN beneran gmn checknya?
    {'nama': 'Andi', 'kota':'Jakarta', 'job':'PNS'},
    ]
df = pd.DataFrame(data)
print(df)
#NaN =not a number

# x = [1,2,3,4,5]
# x = pd.Series(x, name='Test')
# y = [1,2,3,4,5]
# y = pd.Series(y, name='Try')
# df = pd.DataFrame({'Col.X':x, 'Col.Y':y})
# print(df)
# print(x.name)

#name akan jadi nama columns:
x = [1,2,3,4,5]
x = pd.Series(x, name='Test')
y = [1,2,3,4,5]
y = pd.Series(y, name='Try')
df = pd.DataFrame({x.name: x, y.name:y}) #kalo misal males liat nama kolom, pake .name aja
print(df)

## name akan jadi nama row:
x = [1,2,3,4,5]
x = pd.Series(x, name='Test')
y = [1,2,3,4,5]
y = pd.Series(y, name='Try')
df = pd.DataFrame([x,y])
print(df)

df = pd.DataFrame({
    'A': np.arange(20, 26),
    'B': [32,4,12,54,21,18],
    'C': np.random.rand(6),  ##array nya harus sama ada 6 row. jd isinya 6
    'D': np.ones(6)
}, index = list('abcdef'))
print(df)
print(df.head(3)) ##bakal muncul 3 data pertama
print(df.tail(5)) ##bakal muncul 5 data terkahir
print(df.index) 
print(list(df.index))
print(df.columns)
print(df.values)
# print(type(df.values))
print(df.describe())  ##untuk tau statistik nya. mean, std, min, max

print(df)
ab = df['A']+df['B']
print(ab)
print(df['A'].values)
print(df.describe())
# print(df.sort_index(ascending=False, axis=0))  ##axis=0, maka sort bedasarkan index
# print(df.sort_index(ascending=False, axis=1))  ##axis=1, maka sort berdasar columns
# df.sort_index(ascending=False, axis=1, inplace=True)
# #asign value ke daata frame. inplace=True
# #asign value selain dengan: df = df.sort_index(ascending=False, axis=1)
# print(df)
# print(df.sort_values(by='C')) ##ngurutin ascending dari nilai C



# df = pd.DataFrame({
#     'A': np.array([20, 20, 20, 21, 21,21]),
#     'B': [32,4,12,54,21,18],
#     'C': np.random.rand(6),  ##array nya harus sama ada 6 row. jd isinya 6
#     'D': np.ones(6)
# }, index = list('abcdef'))
# print(df.sort_values(by=['A','B'], ascending=[False, True])) ##ngurutin berdasarkan 2 columns
# print(df[['A','D', 'B', 'C']])
# print(df[0:3])  ## kalau [0] aja ga bisa
# print(df.loc['a', ['A', 'B']])  ##berdasar index(row), lalu column
# print(df.loc['a', 'A']) ##berdasar index(row), lalu column

# print(df.iloc[0]) #munculin semua row yang pertama dari semua columns
# print(df.set_index('A')) ##column A dijadiin index, biasanya kalau tanggal dijadiin index(row) or primary key

# df.index = df['A']
# print(df) ##column A bakal jadi index tapi tetep masih ada column A nya

# df.index = list('abcdef')

print(df.loc[:,'A']) ##seluruh row pada column A ##iloc berdasar urutan(angka). kalau loc memunculkan berdasar nama
print(df.iloc[3:5, 0:])  ##iloc berdasar urutan(angka). kalau loc memunculkan berdasar nama
print(df.loc['a'])  ##iloc berdasar urutan(angka). kalau loc memunculkan berdasar nama
# print(df.iloc[0])  ##iloc berdasar urutan(angka). kalau loc memunculkan berdasar nama
# df.columns = ['Nama', 'Nilai', 'Value', 'Rangking']
# print(df)
# print(df.iloc[::2].sort_values(by=['Nilai', 'Value'],
# ascending = [False, True]
# ))#,[['Nama', 'Nilai']])

k = pd.DataFrame([['nsrv', 'survive', 're'], [1,2,3]])
print(k.iloc[1, 0])
# print(k)
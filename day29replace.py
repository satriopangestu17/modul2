import pandas as pd
import numpy as np

# df = pd.read_csv('data29.csv')
# #penggunaan df.replace
# df = df.replace(['-','#'], np.NaN) ##setelah jadi bisa pakai df.fillna('') seperti dibawah
# df = df.fillna('XXX')
# print(df)


# df = pd.read_csv('data29.csv')
# print(df)
# #penggunaan df.replace
# df = df.replace({'-':'+','#': np.NaN}) ##setelah jadi bisa pakai df.fillna('') seperti dibawah
# # df = df.fillna('XXX')  ##kalau mau ubah NaN jadi XXX
# print(df)

# df = pd.read_csv('data29.csv')
# print(df)
# ## kalau di kolom usia ada minus mdan hashtag maka ubah jadi NaN, kolom nama ada hastag diubah jadi NaN
# df = df.replace({'usia':['-','#'],'nama':'#'}, np.NaN) ##setelah jadi bisa pakai df.fillna('') seperti dibawah
# # df = df.fillna('XXX')  ##kalau mau ubah NaN jadi XXX
# print(df)


# df = pd.read_csv('data29.csv')
# print(df)
# ## kalau di kolom usia ada minus mdan hashtag maka ubah jadi NaN, kolom nama ada hastag diubah jadi NaN
# df = df.replace({'usia':['-','#'],'nama':'#'}, {'usia': np.NaN, 'nama':'Anonim'}) ##setelah jadi bisa pakai df.fillna('') seperti dibawah
# # df = df.fillna('XXX')  ##kalau mau ubah NaN jadi XXX
# print(df)

df = pd.read_csv('data29.csv')
print(df)
## replace berdasar kolom usia ffill jadi kebawah yang direplace
df['usia'] = df['usia'].replace(
    to_replace = '-',
    method = 'ffill'
)
print(df)

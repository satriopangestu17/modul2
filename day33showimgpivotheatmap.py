import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as im


# pict = im.imread('led.png')
# print(pict)
# plt.imshow(pict)
# plt.show()  ##ga usah pake print

## pivot untuk pandas csv
df = pd.read_csv('datasales.csv')
df = df.pivot(index='mobil', columns='nama')
print(df)


# print(df)
# fig, p = plt.subplots()
# # plt.imshow(df, cmap='hot') ##hot untuk temanya merah2
# plt.imshow(df, cmap='hot_r') ##hot untuk temanya merah2
# plt.colorbar()
# print(df.columns) ##showing columns 
# print(df.columns[0][1]) ##showing columns 
# print(df.columns.tolist()[:1])
# col = list(map(lambda x: x[1], df.columns.tolist()))
# print(col) ##keluarin mobila, mobilb, mobilc

# i = list(map(lambda x: x, df.index.tolist()))
# print(i)
# # plt.xticks()

# for x in range(len(i)):
#     for y in range(len(col)):
#         p.text(x, y, df.iloc[x, y], color='b', 
#         fontsize=20, ha='center', va='center')

# p.set_xticks(np.arange(len(col)))
# p.set_xticklabels(col)
# p.set_yticks(np.arange(len(i)))
# p.set_yticklabels(i)
# # p.set_ylim(2.5,-0.1,10) utk edit size
# plt.show()  ##ga usah pake print



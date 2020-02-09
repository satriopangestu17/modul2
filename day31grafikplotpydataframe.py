import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'x': [1,2,3,4,5],
    'y': [9,5,7,3,6],
    'z': [2,3,4,5,3]
})
print(df)
plt.figure('Tes', figsize=(10,1))  ##judul file didepan. harus ditauh sebelum plot
plt.plot(df['x'], df[['y', 'z']])  ## gaperlu plot satu2 seperti sebelumnya
plt.grid(True)
plt.xticks(np.arange(5),list('abcdef'), rotation=180)
plt.yticks(np.arange(0, 10, step=2), rotation = 180)

plt.show()
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
df = pd.DataFrame({
    'x': [1,2,3,4,5],
    'y': [9,5,7,3,6],
    'z': [2,3,4,5,3]
})

# df = pd.DataFrame([{
#     'x': [1,2,3,4,5],
#     'y': [9,5,7,3,6],
#     'z': [2,3,4,5,3]
# }, {'x':[1,2], 'y':[3,5], 'z':[5,6]}])
print(df)
plt.plot(df['x'], df[['y', 'z']])  ## gaperlu plot satu2 seperti sebelumnya
plt.grid(True)
plt.xticks(np.arange(5),['0','b','c','d','e'], rotation=180)
plt.yticks(np.arange(0, 10, step=2), rotation = 180)
plt.show()
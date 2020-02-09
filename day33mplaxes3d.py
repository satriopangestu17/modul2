import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d

fig =plt.figure()
p = plt.subplot(111, projection='3d')
data = range(11)
x = np.array(data)

#[x] biar 2 dimensi. reshape jadi 2 dimensi elemen pertama1, elemen -1 untuk ngitung sendiri sampe range 11
p.plot_wireframe(x, x, x.reshape(1,-1), color='r', linestyle=':')
p.scatter(x, x, x.reshape(1,-1), marker='*', color='y', s=50)
p.set_xlabel('sumbu X')
p.set_ylabel('sumbu Y')
p.set_zlabel('sumbu Z')
plt.show()


# bebas = ['j', 'k', 'l', 'm', 'n', 'o']
# for i,v in enumerate(bebas):
#     print(v)
### i= urutan1,2,3,4,5,6 ; v = j,k,l,m,n,o
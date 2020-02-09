import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d

fig = plt.figure()
p = plt.subplot(111, projection='3d')

# x = np.arange(10)
# y = np.arange(10)
# z = np.arange(10)
# dx = np.ones(10) ##bikin list isinya 1 ada 10 buah
# dy = np.ones(10)
# dz = np.arange(10)
# p.scatter(x, y, z)
# p.bar3d(x, y, z) ##mesti di declare
# plt.show()

# x = np.arange(10) #data x
# y = np.arange(10) #data y
# z = np.zeros(10)  # data z isi 0 semua ada 10 buah
# dx = np.ones(10) ##bikin list isinya 1 ada 10 buah
# dy = np.ones(10)
# dz = np.arange(10) #data dz

# p.bar3d(x, y, z, dx, dy, dz) ##mesti di declare dx, dy, dz
# p.set_xlabel('sumbu X')
# p.set_ylabel('sumbu Y')
# p.set_zlabel('sumbu Z')
# plt.show()



# x = np.arange(10) #data x
# y = np.arange(10) #data y
# z = np.ones(10)  # data z isi 1 semua ada 10 buah. akan start dari bawahnya 1. z adalah tingginya
# # dx = np.ones(10) ##bikin list isinya 1 ada 10 buah
# dx = [2,2,2,2,2,2,2,2,2,2] ##bikin list isinya 1 ada 10 buah
# # dy = np.ones(10)
# dy = [2,2,2,2,2,2,2,2,2,2]
# # dz = np.arange(10) #data dz. tinggi plotnya akan mulai dari 1 sampai 10
# dz = np.ones(10) #data dz. tinggi plotnya akan sama

# p.bar3d(x, y, z, dx, dy, dz) ##mesti di declare dx, dy, dz
# p.set_xlabel('sumbu X')
# p.set_ylabel('sumbu Y')
# p.set_zlabel('sumbu Z')
# plt.show()


x = np.arange(10) #data x
y = np.arange(10) #data y
z = np.zeros(10)  # data z isi 1 semua ada 10 buah. akan start dari bawahnya 1. z adalah tingginya
dx = np.ones(10) ##bikin list isinya 1 ada 10 buah
# dx = [2,2,2,2,2,2,2,2,2,2] ##bikin list isinya 1 ada 10 buah
dy = np.ones(10)
# dy = [2,2,2,2,2,2,2,2,2,2]
# dz = np.arange(10) #data dz. tinggi plotnya akan mulai dari 1 sampai 10
dz = np.arange(10) #data dz. tinggi plotnya akan sama

p.bar3d(x, y, z, dx, dy, dz,
color = ['purple','r','pink','orange','y','g',
'lightgreen','b','lightblue','k']) ##mesti di declare dx, dy, dz
p.set_xlabel('sumbu X')
p.set_ylabel('sumbu Y')
p.set_zlabel('sumbu Z')
# p.set_yticks([1,2])
# p.set_ylim3d(top=2, bottom=1.8)
plt.show()

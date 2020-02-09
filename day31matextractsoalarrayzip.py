import matplotlib.pyplot as plt
import numpy as np

## aray agar ketika di print tidaj ada koma lagi
##dan juga array ketika dioperasikan bisa langsung, example:
x = np.array([1,2,3,4,5,6,7,8,9])
print(x)
y = x ** 2
z = x ** 3
plt.plot(x,y) 
plt.plot(x,z) 
plt.plot(x,x,x,y,x,z)
plt.title('Testing')
plt.xlabel('nilai X')
plt.ylabel('nilai Y / Z')
plt.grid(True)
plt.legend(['Garis XX','Garis XY', 'Garis XZ'], loc = 0)
plt.show()


# $ tar -zxvf Ujian_Digimon_Recommendation.zip 
# $ tar -zxvf DS_Rekomendasi_Buku_Bagus-master.zip 
# $ tar -zxvf Pokemon_Battle-mastermattnicholas.zip 
# $ tar -zxvf Ujian_Pemain_Bola-master.zip  
# $ tar -zxvf DS_Pokemon_Battle-master.zip
# $ tar -zxvf Ujian_Digimon_Recommendationandrew.zip
# ##*wajib tar untuk extract, ga bisa cara extract biasa
# $ sudo mkdir -p /data/db   #untuk bikin folder. cuma sekali aja
# $ cd mongodb-osx-xxx/bin

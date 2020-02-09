import numpy as np

# x = np.loadtxt('0.csv')  ##bisa baca asal number
# # print(type(x))
# print(x)

x = np.loadtxt('1.csv', skiprows=1, delimiter=',')  ##bkalau angka pake koma such as 2,20 ga bisa kebaca
# print(type(x))
print(x)


x = np.loadtxt('1.csv', skiprows=1, delimiter=',', unpack=True)  ##unpack true untuk jadiin 2 row saja
# print(type(x))
print(x)

a, b =12, 13
print(a)
print(b)


id, usia = np.loadtxt('1.csv', skiprows=1, delimiter=',', unpack=True)  ##unpack true untuk jadiin 2 row saja
# print(type(x))
# print(id)
# print(usia)
# np.savetxt('4.csv',(id, usia), fmt='%d',  #%d untuk jadi integer
# header = 'usia', comments='@')

print(id)
print(usia)



data = np.loadtxt('1.csv', skiprows=1, delimiter=',')  
np.savetxt('4.csv', data, fmt='%d',  #%d untuk jadi integer
header = 'id,usia', comments='')



#coba pake lambda
data1 = np.array(list(map(lambda a,b: [a,b], id, usia)))

np.savetxt('5.csv', data1, fmt='%d',
header='id,usia', comments='', delimiter=',')
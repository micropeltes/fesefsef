jarak = int(input('jarak:'))
try:
    ival = int(jarak)
except:
    ival = -1
    print('not a number')
    
kendaraan =input('kendaraan yang digunakan:')

if kendaraan=='mobil':
    print((jarak)/80,'jam')
elif kendaraan=='motor':
    print((jarak)/40,'jam')
elif kendaraan=='sepeda':
    print((jarak)/15,'jam')
else :
    print("kendaraan tidak diketahui")
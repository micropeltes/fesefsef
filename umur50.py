nama=input('Masukkan nama = ')
usia=int(input('Masukkan usia = '))
try:
    ival = int(usia)
except:
    ival = -1
    print('not a number')
umur=50-usia
umur3=2021+umur
umur2=str(umur3)
print(nama +' akan berusia 50 pada tahun '+ umur2)
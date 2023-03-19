angka= int(input('masukkan angka yang akan dicari factornya: '))
for angka_hitung in range(1, angka+1):
    if angka % angka_hitung == 0:
        print(angka_hitung)
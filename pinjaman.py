pinj =int((input("masukkan jumlah pinjaman: Rp.")))
bunga =int((input("masukkan bunga (dalam persen): ")))
lama =int((input("masukkan lama pinjaman(dalam bulan): ")))
pers_bga = bunga/100
total_bga = pers_bga*lama
bgabga = pinj*total_bga
total_htg= pinj+bgabga
print("Rp.",int(total_htg),",00")
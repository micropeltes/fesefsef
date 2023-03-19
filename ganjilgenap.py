angka= input("angka= ")
try:
    ival = int(angka)
    if int(angka) % 2 == 0 :
        print("genap")
    else :
        print("ganjil")
except:
    ival = -1
    print('not a number, masukkan ulang')

print('KALKULATOR SEDERHANA')
print('====================')
print('1. Penjumlahan')
print('2. Pengurangan')
print('3. Perkalian')
print('4. Pembagian')
print('5. Exponential')
print('6. Selesai')
print('====================')
line = input('pilih (1-6) ==>')
if line[0] == '1' :
#penjumlahan
    tambah1 = input('masukkan angka 1 = ')
    try:
        ival = int(tambah1)
    except:
        ival = -1
        print('not a number')
    tambah2 = input('masukkan angka 2 = ')
    try:
        ival = int(tambah1)
        print('Penjumlahan dari',int(tambah1),' dengan ',int(tambah2),'adalah',int(tambah1)+int(tambah2))
    except:
        ival = -1
        print('not a number, masukkan ulang')

if line[0] == '2' :
#pengurangan
    kurang1 = input('masukkan angka 1 = ')
    try:
        ival = int(kurang1)
    except:
        ival = -1
        print('not a number')
    kurang2 = input('masukkan angka 2 = ')
    try:
        ival = int(kurang1)
        print('Pebgurangan dari',int(kurang1),' dengan ',int(kurang2),'adalah',int(kurang1)-int(kurang2))
    except:
        ival = -1
        print('not a number, masukkan ulang')

if line[0] == '3' :
#perkalian
    angka1 = input('masukkan angka 1 = ')
    try:
        ival = int(angka1)
    except:
        ival = -1
        print('not a number')
    angka2 = input('masukkan angka 2 = ')
    try:
        ival = int(angka1)
        print('Perkalian dari',int(angka1),' dengan ',int(angka2),'adalah',int(angka1)*int(angka2))
    except:
        ival = -1
        print('not a number, masukkan ulang')
if line[0] == '4' :
#pembagian
    bagi1 = input('masukkan angka 1 = ')
    try:
        ival = int(bagi1)
    except:
        ival = -1
        print('not a number')
    bagi2 = input('masukkan angka 2 = ')
    try:
        ival = int(bagi1)
        print('Pembagian dari',int(bagi1),' dengan ',int(bagi2),'adalah',int(bagi1)/int(bagi2))
    except:
        ival = -1
        print('not a number, masukkan ulang')
        
if line[0] == '5' :
#exponential
    exp1 = input('masukkan angka 1 = ')
    try:
        ival = int(exp1)
    except:
        ival = -1
        print('not a number')
    exp2 = input('masukkan angka 2 = ')
    try:
        ival = int(exp1)
        print('Nilai pangkat dari',int(exp1),' dengan ',int(exp2),'adalah',int(exp1)**int(exp2))
    except:
        ival = -1
        print('not a number, masukkan ulang')
if line[0] == '6' :
#selesai
    print('selesai')
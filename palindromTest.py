print('PALINDROM TESTING')
print('======================')
kata_awal = input("Masukkan kata atau kalimat yang akan di test = ")
panjang_kata = len(kata_awal)
kata_inverse = "";
i = panjang_kata-1
while i>-1:
    kata_inverse = kata_inverse + kata_awal[i]
    i=i-1
if kata_inverse == kata_awal:
    print(kata_awal,' adalah palindrom, dengan hasil dibaliknya adalah:',kata_inverse)
else:
    print(kata_awal,' bukan palindrom, dengan hasil dibaliknya adalah:',kata_inverse)
    
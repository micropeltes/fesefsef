kata = input('Masukkan sebuah kata/kalimat = ')
unik=''
kata2= ''
for i in kata:
    if i not in unik:
        unik+=i
for i in unik:
    counter=0
    for j in kata:
        if i == j:
            counter+=1
#pengubah
        if counter >= 2:
            unik += "$"
        print(unik)
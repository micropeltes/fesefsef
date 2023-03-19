s = input('Masukkan sebuah kata/kalimat = ')
unik=''
for i in s:
    if i not in unik:
        unik+=i
    
flag = False
for i in unik:
    sf = ''
    for j in s:
        if i == j:
            if not flag:
                flag = True
                sf += j
            else:
                sf += '$'
        else:
            sf += j
    flag = False
    s = sf
print(sf)
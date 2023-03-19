inp = input('masukkan string : ')
inp2 = input('masukkan string kedua : ')
pnj = len(inp)

a= pnj % 2
b= int(pnj / 2)

a2= inp[0:b]
b2= inp2
c2= inp[b:pnj]
d2= a2+b2+c2

if a == 0 :
    print(d2)
else :
    print(d2)
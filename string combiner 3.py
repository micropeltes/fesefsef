inp = input('masukkan string : ')
inp2 = input('masukkan string kedua : ')
inp3 = input('masukkan string ketiga : ')
pnj = len(inp)
pnj2 = len(inp2)
pnj3 = len(inp3)

w= int(pnj / 2)
w2= int(pnj2 / 2)
w3= int(pnj3 / 2)

a= inp[0]
a2= inp2[0]
a3= inp3[0]

b= inp[w]
b2= inp2[w2]
b3= inp3[w3]

c= inp[pnj-1]
c2= inp2[pnj2-1]
c3= inp3[pnj3-1]

print(a+a2+a3+b+b2+b3+c+c2+c3)
n = int(input("Masukkan N = "))
p=('*')
y=(' ')

for pattern1 in range (0,n):
    for pattern2 in range (pattern1):
        print(p, end="")
    print(y)

for pattern1 in range (n,0,-1):
    for pattern2 in range (pattern1):
        print(p, end="")
    print(y)
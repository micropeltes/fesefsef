i=0
j=0
a=True
while a == True:
    print("pilih opsi di bawah ini")
    print('a = gunting')
    print('b = batu')
    print('c = kertas')
    R = input("ketik disini :")
    if R == "a":
        print("batu")
        print("Kamu kalah HAHAHA")
        i=i+1
    elif R == "b":
        print("kertas")
        print("Kamu kalah HAHAHA")
        i=i+1
    elif R == "c":
        print("gunting")
        print("Kamu kalah HAHAHA")
        i=i+1
    else:
        print("masukin huruf yang bener")
        j=j+1
    print("anda sudah kalah",(i),"kali")
    print("anda sudah salah masukin huruf",(j),"kali")
if R == 'e':
    a=False
else:
    a=True
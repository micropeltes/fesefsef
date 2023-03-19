aa= input("angka= ")
try:
    ival = int(aa)
except:
    ival = -1
    print('not a number')
angka= int(aa)
if angka > 1:
    for pembagi in range(2,angka):
        if (angka % pembagi) == 0:
            print(angka,"bukan bilangan prima")
            print(angka," = ",pembagi," x ",angka//pembagi)
            break
    else:
        print(aa,"adalah bilangan prima")
sisi1 = int(input('sisi 1:'))
try:
    ival = int(sisi1)
except:
    ival = -1
    print('not a number')
    
sisi2 = int(input('sisi 2:'))
try:
    ival = int(sisi2)
except:
    ival = -1
    print('not a number')
    
sisi3 = int(input('sisi 3:'))
try:
    ival = int(sisi3)
except:
    ival = -1
    print('not a number')
    
if sisi1==sisi2 and sisi1==sisi3 and sisi2==sisi3:
    print('segitiga sama sisi')
elif sisi1!=sisi2 and sisi1!=sisi3 and sisi2!=sisi3:
    print('segitiga sembarang')
else:
    print('segitiga sama kaki')
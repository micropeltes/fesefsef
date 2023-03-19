umur = input('umur anjing:')
try:
    ival = int(umur)
except:
    ival = -1
    print('not a number')

if int(umur) <= 2:
    umur1 =(int(umur)*10.5)
    print('umur anjing dalam satuan umur manusia:',umur1)
    
else :
    umur2 = float(10.5*2)+(float((int(umur)-2)*4))
    print('umur anjing dalam satuan umur manusia:',umur2)
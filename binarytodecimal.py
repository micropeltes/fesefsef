bi = input('Masukkan bilangan biner= ')
if len(bi)==4:
    a=int(bi[3])
    b=int(bi[2])*2
    c=int(bi[1])*4
    d=int(bi[0])*8
    print(a+b+c+d)
elif len(bi)==3:
    b=int(bi[2])
    c=int(bi[1])*2
    d=int(bi[0])*4
    print(b+c+d)
elif len(bi)==2:
    c=int(bi[1])
    d=int(bi[0])*2
    print(c+d)
elif len(bi)==1:
    print(bi[0])
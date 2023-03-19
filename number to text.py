R = input('Masukkan angka= ')
if len(R)==4:
    a=(R[0])
    b=(R[1])
    c=(R[2])
    d=(R[3])
    J=(a+" thousand ")

elif len(R)==4:
    a=(R[0])
    b=(R[1])
    c=(R[2])
    d=(R[3])
    J=(a+" thousand "+b+" hundred ")

elif len(R)==4:
    a=(R[0])
    b=(R[1])
    c=(R[2])
    d=(R[3])
    J=(a+" thousand "+b+" hundred "+c)

elif len(R)==4:
    a=(R[0])
    b=(R[1])
    c=(R[2])
    d=(R[3])
    J=(a+" thousand "+b+" hundred "+c+"-"+d)
    
elif len(R)==3:
    b=(R[0])
    c=(R[1])
    d=(R[2])
    J=(b+c+d)
    
elif len(R)==2:
    c=(R[0])
    d=(R[1])
    J=(c+d)
    
elif len(R)==1:
    J=(R[0])
    

print(J)
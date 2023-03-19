inp = input('masukkan kata : ')
pnj = len(inp)
if pnj % 2 == 0 :
    a = pnj/2
    x = a-2
    print(inp[int(x):int(a)+1])
else :
    a = (pnj+1)/2
    x=a-2
    print(inp[int(x):int(a)+1])
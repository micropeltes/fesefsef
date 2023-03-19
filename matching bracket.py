inp = input('masukkan string : ')
a = '()'
b = '[]'
c = '{}'
C1 = 0
C2 = 0
C3 = 0
for asa in inp:
    if asa in a:
        C1+=1
for asa in inp:
    if asa in b:
        C2+=1
for asa in inp:
    if asa in c:
        C3+=1
        
#if C1%2 == 0:
#    print(' Yang memiliki pasangan ',a, ' = ',int(C1/2))
#else:
#    print(' Yang tidak memiliki pasangan ' ' = ',C1)
#if C2%2 == 0:
#    print(' Yang memiliki pasangan ',a, ' = ',int(C2/2))
#else:
#    print(' Yang tidak memiliki pasangan ' ' = ',C2)

#if C3%2 == 0:
#    print(' Yang memiliki pasangan ',a, ' = ',int(C3/2))
#else:
#    print(' Yang tidak memiliki pasangan ' ' = ',C3)
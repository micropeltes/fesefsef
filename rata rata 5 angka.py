inp1 = input('angka 1:')
try:
    ival = int(inp1)
except:
    ival = -1
    print('not a number')
    
inp2 = input('angka 2:')
try:
    ival = int(inp2)
except:
    ival = -1
    print('not a number')
    
inp3 = input('angka 3:')
try:
    ival = int(inp3)
except:
    ival = -1
    print('not a number')
    
inp4 = input('angka 4:')
try:
    ival = int(inp4)
except:
    ival = -1
    print('not a number')
    
inp5 = int(input('angka 5:'))
try:
    ival = int(inp5)
except:
    ival = -1
    print('not a number')
    
rata2 = ((int(inp1)+int(inp2)+int(inp3)+int(inp4)+inp5)/5)

print(rata2)

if rata2>=80 and rata2<=100:
    print('A')
elif rata2 >= 70 and rata2<=79:
    print('B')
elif rata2>=6 and rata2<=69:
    print('C')
elif rata2>=40 and rata2<=59:
    print('D')
elif rata2<=39:
    print('E')
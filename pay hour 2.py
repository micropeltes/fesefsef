hours = input('hours:')
try:
    ival = int(hours)
except:
    ival = -1
    print('not a number')

rate = input('rate:')
try:
    ival = int(rate)
except:
    ival = -1
    print('not a number')

if int(hours) <= 40:
    ratex = int(hours)*int(rate)
    print('pay',ratex)
    
else :
    ratey = float(40*int(rate))+(float(int(hours)-(40)))*(float(int(rate)*1.5))
    print('pay',ratey)
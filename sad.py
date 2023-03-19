from tracemalloc import stop


lis=[]
stop = False
i=0
while (not stop):
    asd=int(input("input:".format(i)))
    lis.append(asd)

    i+=1

    if asd==0:
        stop = True

def sumOfList(list, size):
   if (size == 0):
     return 0
   else:
     return list[size - 1] + sumOfList(list, size - 1)
  
# Driver code    
total = sumOfList(lis, len(lis))
 
print("output: ", total)
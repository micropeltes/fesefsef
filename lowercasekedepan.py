inp = input('masukkan string : ')
low =str()
up =str()
for i in inp:
    if i.islower():
        low+=i

for a in inp:
    if a.isupper():
        up+=a
        
print(low+up)    
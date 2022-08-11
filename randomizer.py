import string
import random
import colorama
from colorama import Fore, Style, Back

inp = int(input("panjang text: "))
inp2= int(input("berapa banyak: "))


x=0

def ar(size=inp, chars=string.printable):
    return ''.join(random.choice(chars) for _ in range(size))

while x<inp2:
    print(Fore.GREEN + Style.BRIGHT + ar())
    x=x+1
print(Fore.YELLOW + Style.BRIGHT + Back.BLUE +"Done...")
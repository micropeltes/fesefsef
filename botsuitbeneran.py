import string
import random
import colorama
from colorama import Fore, Back, Style
#list
a = ["gunting","batu","kertas"]
x=0
while x<1:
    #pilihan permainan
    print("1. suit")
    print("2. randomizer")
    inpo=input("anda ingin memainkan permainan apa?:")
    if(inpo=="1"):
        #input
        print("1. Gunting")
        print("2. Batu")
        print("3. Kertas")
        asd =(input("pilih salah satu dari nomor di atas:"))
        if(asd=="1"):
            inp="gunting"

        elif(asd=="2"):
            inp="batu"

        elif(asd=="3"):
            inp="kertas"

        else:
            print(("input anda salah"))
            
        print("input anda adalah: " + inp)
        #randomizer
        def ar(size=1,chars=a):
            return ''.join(random.choice(chars) for _ in range(size))

        #perbandingan gunting batu kertas
        if(inp==ar()):
            print(ar())
            print(Fore.YELLOW + 'seri')

        elif(inp=='gunting'):
            print(ar())
            if ar()=='batu':
                print(Back.RED + "anda kalah") 
                print(Style.RESET_ALL)
            elif ar()=='kertas':
                print(Fore.CYAN + Style.BRIGHT + 'anda menang')
                print(Style.RESET_ALL)

        elif(inp=='batu'):
            print(ar())
            if ar()=='kertas':
                print(Back.RED + "anda kalah") 
                print(Style.RESET_ALL)
            elif ar()=='gunting':
                print(Fore.CYAN + Style.BRIGHT + 'anda menang')
                print(Style.RESET_ALL)

        elif(inp=='kertas'):
            print(ar())
            if ar()=='gunting':
                print(Back.RED + "anda kalah") 
                print(Style.RESET_ALL)
            elif ar()=='batu':
                print(Fore.CYAN + Style.BRIGHT + 'anda menang')
                print(Style.RESET_ALL)

        else:
            print('input anda salah')

        #looping
        bah=input('ingin bermain lagi?(Y/n):')
        blah=bah.lower()
        if(blah=='y'):
            x=x

        elif(blah=='n'):
            x=x+1

        else:
            print("input anda salah")
            bah=input('ingin bermain lagi?(Y/n):')
            blah=bah.lower()
            if(blah=='y'):
                x=x

            elif(blah=='n'):
                x=x+1
    elif(inpo=="2"):
        print("1. randomizer benar-benar random")
        print("2. randomizer huruf")
        print("3. randomizer angka")
        jkjk=input("Pilih salah satu pilihan diatas: ")
        if(jkjk=="1"):
            inp = int(input("panjang text: "))
            inp2= int(input("berapa banyak: "))

            y=0

            def ar(size=inp, chars=string.printable):
                return ''.join(random.choice(chars) for _ in range(size))

            while y<inp2:
                print(Fore.GREEN + Style.BRIGHT + ar())
                y=y+1
            print(Fore.YELLOW + Style.BRIGHT + Back.BLUE +"Done...")
            print(Style.RESET_ALL)

            #looping
            bah=input('ingin bermain lagi?(Y/n):')
            blah=bah.lower()
            if(blah=='y'):
                x=x

            elif(blah=='n'):
                x=x+1

            else:
                print("input anda salah")
                bah=input('ingin bermain lagi?(Y/n):')
                blah=bah.lower()
                if(blah=='y'):
                    x=x

                elif(blah=='n'):
                    x=x+1
        elif(jkjk=="2"):
            inp = int(input("panjang text: "))
            inp2= int(input("berapa banyak: "))
            print("1. semua huruf kecil")
            print("2. semua huruf besar")
            print("3. campur")
            inp3= input("Pilih salah satu pilihan diatas: ")

            y=0

            if (inp3=="1" or "2" or "3"):
                def ar(size=inp, chars=string.ascii_lowercase):
                    return ''.join(random.choice(chars) for _ in range(size))

            while y<inp2:
                print(Fore.GREEN + Style.BRIGHT + ar())
                y=y+1
            print(Fore.YELLOW + Style.BRIGHT + Back.BLUE +"Done...")
            print(Style.RESET_ALL)

            #looping
            bah=input('ingin bermain lagi?(Y/n):')
            blah=bah.lower()
            if(blah=='y'):
                x=x

            elif(blah=='n'):
                x=x+1

            else:
                print("input anda salah")
                bah=input('ingin bermain lagi?(Y/n):')
                blah=bah.lower()
                if(blah=='y'):
                    x=x

                elif(blah=='n'):
                    x=x+1
        elif(jkjk=="3"):
            inp = int(input("panjang text: "))
            inp2= int(input("berapa banyak: "))

            y=0

            def ar(size=inp, chars=string.octdigits):
                return ''.join(random.choice(chars) for _ in range(size))

            while y<inp2:
                print(Fore.GREEN + Style.BRIGHT + ar())
                y=y+1
            print(Fore.YELLOW + Style.BRIGHT + Back.BLUE +"Done...")
            print(Style.RESET_ALL)

            #looping
            bah=input('ingin bermain lagi?(Y/n):')
            blah=bah.lower()
            if(blah=='y'):
                x=x

            elif(blah=='n'):
                x=x+1

            else:
                print("input anda salah")
                bah=input('ingin bermain lagi?(Y/n):')
                blah=bah.lower()
                if(blah=='y'):
                    x=x

                elif(blah=='n'):
                    x=x+1
    else:
        print("input anda salah")
        x=x
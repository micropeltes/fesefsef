#Prajnagastya Adhyatmika dan Kristoforus Gwayne Donovan Muliadi
x=0
y=int(input('berapa banyak anda ingin melakukan kalkulasi umur: '))
thnini=int(input("masukkan tahun hari ini:"))
blnini=int(input("masukkan bulan hari ini:"))
hrini=int(input("masukkan tanggal hari ini:"))

while y>x:
    tahun=int(input("masukkan tahun lahir anda: "))
    strbln='masukkan bulan lahir anda: '
    strhr='masukkan tanggal lahir anda: '
    erorcode="tanggal yang anda masukkan salah"
    if tahun%4:
        bulan=int(input(strbln))
        if bulan>12:
            print(erorcode)
        elif bulan<8:
            if bulan==2:
                hari=int(input(strhr))
                if hari>29:
                    print(erorcode)
            elif bulan%2==1:
                hari=int(input(strhr))
                if hari>32:
                    print(erorcode)
            else:
                hari=int(input(strhr))
                if hari>31:
                    print(erorcode)
        elif bulan>=8:
            if bulan%2==1:
                hari=int(input(strhr))
                if hari>31:
                    print(erorcode)
            else:
                hari=int(input(strhr))
                if hari>32:
                    print(erorcode)
    else:
        bulan=int(input(strbln))
        if bulan>12:
            print("bulan"+erorcode)
        elif bulan<8:
            if bulan==2:
                hari=int(input(strhr))
                if hari>28:
                    print(erorcode)
            elif bulan%2==1:
                hari=int(input(strhr))
                if hari>32:
                    print(erorcode)
            else:
                hari=int(input(strhr))
                if hari>31:
                    print(erorcode)
        elif bulan>=8:
            if bulan%2==1:
                hari=int(input(strhr))
                if hari>31:
                    print(erorcode)
            else:
                hari=int(input(strhr))
                if hari>32:
                    print(erorcode)

    fgsthn=thnini-tahun
    fgsbln=blnini-bulan
    fgshr=hrini-hari
    if fgsbln or fgshr >=0:
        print("umur anda",fgsthn,"tahun",fgsbln,"bulan",fgshr,"hari")
        x+=1
    else:
        print("umur anda",fgsthn,"tahun",fgsbln,"kurang bulan",fgshr,"kurang hari")
        x+=1
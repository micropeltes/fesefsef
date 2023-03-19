ag1= int(input('masukkan angka ke-1: '))
ag2= int(input('masukkan angka ke-2: '))
ag3= int(input('masukkan angka ke-3: '))
ag4= int(input('masukkan angka ke-4: '))
ag5= int(input('masukkan angka ke-5: '))
ag6= int(input('masukkan angka ke-6: '))
ag7= int(input('masukkan angka ke-7: '))
ag8= int(input('masukkan angka ke-8: '))
ag9= int(input('masukkan angka ke-9: '))
ag10= int(input('masukkan angka ke-10: '))
kecil=999999999999999999999
#rata-rata
rata=(ag1+ag2+ag3+ag4+ag5+ag6+ag7+ag8+ag9+ag10)/10
print(rata)
#nilai terbesar
if ag1<ag2:
    big=ag2
if big<ag3:
    big=ag3
if big<ag4:
    big=ag4
if big<ag5:
    big=ag5
if big<ag6:
    big=ag6
if big<ag7:
    big=ag7
if big<ag8:
    big=ag8
if big<ag9:
    big=ag9
if big<ag10:
    big=ag10
print(big)
#nilai terkecil
if ag1>ag2:
    kecil=ag2
if kecil>ag3:
    kecil=ag2
if kecil>ag4:
    kecil=ag4
if kecil>ag5:
    kecil=ag5
if kecil>ag6:
    kecil=ag6
if kecil>ag7:
    kecil=ag7
if kecil>ag8:
    kecil=ag8
if kecil>ag9:
    kecil=ag9
if kecil>ag10:
    kecil=ag10
print(kecil)

# math metodunu kullanarak gelişmiş hesap makinesi yapalım.

# 1. işlem=toplama
# 2. işlem=çıkarma
# 3. işlem=çarpma
# 4. işlem=bölme
# 5. işlem=üst alma
# 6. işlem=exp alma
# 7. işlem=karekök alma
# 8. işlem=sin alma
# 9. işlem=cos alma
# 10.işlem=tan alma
# 11.işlem=log10 alma
# 12.işlem=faktoriyel alma


import math

while True:

    islem = int(input(" hangi numaralı işlemi yapmak istiyorsunuz ? : "))

    if islem == 0 :
        break

    elif islem==1:
        sayi1=float(input("sayı giriniz: "))
        sayi2=float(input("sayı giriniz: "))
        print(" {} ile {} toplamı : {} ".format(sayi1,sayi2,sayi1+sayi2))
    elif islem==2:
        sayi1 = float(input("sayı giriniz: "))
        sayi2 = float(input("sayı giriniz: "))
        print(" {} - {} = {} ".format(sayi1, sayi2, sayi1 - sayi2))
    elif islem==3:
        sayi1 = float(input("sayı giriniz: "))
        sayi2 = float(input("sayı giriniz: "))
        print(" {} * {} = {} ".format(sayi1, sayi2, sayi1*sayi2))
    elif islem==4:
        sayi1 = float(input("sayı giriniz: "))
        sayi2 = float(input("sayı giriniz: "))
        print(" {} / {} = {} ".format(sayi1, sayi2, sayi1/sayi2))
    elif islem==5:
        sayi1 = float(input("sayı giriniz: "))
        ust = float(input("üssü giriniz: "))
        x=math.pow(sayi1,ust)
        print("{} üssü {} = {}".format(sayi1,ust,x))
    elif islem==6:
        sayi1=float(input("sayı giriniz: "))
        x=math.exp(sayi1)
        print("{} exponeyeli ={}".format(sayi1,x))
    elif islem==7:
        sayi1=float(input("sayı giriniz: "))
        x=math.sqrt(sayi1)
        print("{} karekökü ={}".format(sayi1,x))
    elif islem==8:
        sayi1=float(input("sayı giriniz: "))
        x=math.sin(sayi1)
        print("{} sinüsü ={} ".format(sayi1,x))
    elif islem==9:
        sayi1 = float(input("sayı giriniz: "))
        x=math.cos(sayi1)
        print("{} cosünüsü ={}".format(sayi1,x))
    elif islem==10:
        sayi1 = float(input("sayı giriniz: "))
        x=math.tan(sayi1)
        print("{} tanjantı ={}".format(sayi1,x))
    elif islem==11:
        sayi1 = float(input("sayı giriniz: "))
        x=math.log10(sayi1)
        print("{} 10 tabanında logaritması ={}".format(sayi1,x))
    elif islem==12:
        sayi1 = float(input("sayı giriniz: "))
        x=math.factorial(sayi1)
        print("{} faktoriyeli ={}".format(sayi1,x))


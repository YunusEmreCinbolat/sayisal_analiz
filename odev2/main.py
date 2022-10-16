#1.soru)
iterasyon_sayisi=int(input("iterasyon sayisini giriniz "))
alt_sinir=int(input("alt siniri giriniz "))
ust_sinir=int(input("ust siniri giriniz: "))
kok=True
for i in range(0,iterasyon_sayisi):
    ust_deger=(ust_sinir**3)-(2*(ust_sinir**2))-5
    alt_deger=(alt_sinir**3)-(2*(alt_sinir**2))-5
    if(alt_deger*ust_deger<0):
        orta_kok=(alt_sinir+ust_sinir)/2
        orta_deger=(orta_kok**3)-(2*(orta_kok**2))-5
        if(orta_deger*ust_deger<0):
            alt_sinir=orta_kok
        else:
            ust_sinir=orta_kok
    else:
        kok=False
if kok==True:
    print(f'alt sinir: {alt_sinir} ------ ust sinir: {ust_sinir} ----------- iterasyon degeri: {(alt_sinir+ust_sinir)/2}')
else:
    print("kok yoktur")

# 2.soru)

iterasyon_sayisi2=0
alt_sinir1=int(input("alt siniri giriniz "))
ust_sinir1=int(input("ust siniri giriniz: "))
kok2=True
orta_kok1=(alt_sinir1+ust_sinir1)/2
cıkıs=False
while(cıkıs==False):
    ust_deger1=(ust_sinir1**3)+(4*(ust_sinir1**2))-10
    alt_deger1=(alt_sinir1**3)+(4*(alt_sinir1**2))-10
    if(alt_deger1*ust_deger1<0):
        orta_kok1=(alt_sinir1+ust_sinir1)/2
        orta_deger1=(orta_kok1**3)+(4*(orta_kok1**2))-10
        if(orta_deger1*ust_deger1<=0):
            alt_sinir1=orta_kok1
        else:
            ust_sinir1=orta_kok1
        if(abs(orta_kok1-(alt_sinir1+ust_sinir1)/2)<0.000001):
            cıkıs=True
    else:
        kok2=False
        break
    iterasyon_sayisi2+=1
if kok2==True:
    print(f'alt sinir: {alt_sinir1} ------ ust sinir: {ust_sinir1} ------- cevap: {(ust_sinir1+alt_sinir1)/2} ')
    print(f'iterasyon sayisi: {iterasyon_sayisi2}')
else:
    print("kok yoktur")

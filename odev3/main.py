iterasyon_sayisi=int(input("Iterasyon sayisini giriniz: "))
taban=4
us=0.5
kok=2
bolen_taban=taban
for i in range(0,iterasyon_sayisi):
        bolen_taban = bolen_taban * -us
        kok = kok - ((taban / (2.71 ** (us * kok)) - kok) / (bolen_taban / (2.71 ** (us * kok))-1))
print(kok)
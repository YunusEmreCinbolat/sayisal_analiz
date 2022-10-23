#1-)
iterasyon_sayisi=int(input("Iterasyon sayisini giriniz: "))
taban=4
us=0.5
kok=2
bolen_taban=taban* -us
for i in range(0,iterasyon_sayisi):
        kok = kok - ((taban / (2.71 ** (us * kok)) - kok) / (bolen_taban / (2.71 ** (us * kok))-1))
print(kok)
#2-)

# x^1/3 denkleminde newton rapson yöntemi ile çözersek ilk kök değerine 2 verdiğimizde sonuç 0,5 çıkar
# ve bu adımları devam ettirirsek 0 a yaklaşır aynı şekilde kök negatif olsa bile 0 a yaklaşır
import math
terim=int(input("Terim sayısı: "))
mccluinhesabı=1
for i in range(2,terim+1,2):
    mccluinhesabı-=((math.pi/5)**i)/math.factorial(i)
gercek_deger=math.cos(math.pi/5);
kesme_hata=gercek_deger-mccluinhesabı
print("Gerçek değer: ",gercek_deger)
print("Taylor değeri: ",mccluinhesabı)
print(f"{terim} li taylor acilimi kesme hatası: ",kesme_hata)
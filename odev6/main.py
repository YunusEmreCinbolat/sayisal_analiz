#1-)
import math
kok=1
h=0.2

ileri_fark=(1/(2*h))*(-3*(math.exp(kok))+4*(math.exp(kok+h))-1*(math.exp(kok+(2*h))))
print(f"ileri_fark: {ileri_fark}")

geri_fark=(1/(2*(-h)))*(-3*(math.exp(kok))+4*(math.exp(kok+(-h)))-1*(math.exp(kok+(2*(-h)))))
print(f"geri_fark: {geri_fark}")

merkezi_fark=(1/(2*h))*(math.exp(kok+h)-math.exp(kok-h))
print(f"merkezi_fark: {merkezi_fark}")

analitik_sonuc=math.exp(kok)
print(f"Analitik cozum: {analitik_sonuc}")
print(f"Ileri fark - Analitik sonuc: {abs(ileri_fark-analitik_sonuc)}")
print(f"Geri fark - Analitik sonuc: {abs(geri_fark-analitik_sonuc)}")
print(f"Merkezi fark - Analitik sonuc: {abs(merkezi_fark-analitik_sonuc)}")

#3
#a-) h=0.1 için
kok1=1
h1=0.1
analitik_sonuc1=kok1**3
Ileri_fark=(1/(2*h1))*((-3*(kok1**3))+(4*((kok1+h1)**3))-(1*((kok1+(2*h1))**3)))
print(f"ileri fark: {Ileri_fark}")
print(f"Ileri fark - Analitik sonuc: {abs(Ileri_fark-analitik_sonuc1)} ")

Geri_fark=(1/(2*(-h1))*((-3*(kok1**3))+(4*((kok1-h1)**3))-(1*((kok1+(2*(-h1))**3)))))
print(f"Geri fark: {Geri_fark}")
print(f"Geri fark - Analitik sonuc: {abs(Geri_fark-analitik_sonuc1)} ")


Merkezi_fark=(1/(2*h1)*(((kok1+h1)**3)-((kok1-h1)**3)))
print(f"Merkezi fark: {Merkezi_fark}")
print(f"Merkezi fark - Analitik sonuc: {abs(Merkezi_fark-analitik_sonuc1)} ")

#3-b h=0.2 için
kok2=1
h2=0.2
analitik_sonuc2=kok2**3
Ileri_fark1=(1/(2*h2))*((-3*(kok2**3))+(4*((kok2+h2)**3))-(1*((kok2+(2*h2))**3)))
print(f"ileri fark: {Ileri_fark1}")
print(f"Ileri fark - Analitik sonuc: {abs(Ileri_fark1-analitik_sonuc2)} ")

Geri_fark1=(1/(2*(-h2))*((-3*(kok2**3))+(4*((kok2-h2)**3))-(1*((kok2+(2*(-h2))**3)))))
print(f"Geri fark: {Geri_fark1}")
print(f"Geri fark - Analitik sonuc: {abs(Geri_fark1-analitik_sonuc2)} ")


Merkezi_fark1=(1/(2*h2)*(((kok2+h2)**3)-((kok2-h2)**3)))
print(f"Merkezi fark: {Merkezi_fark1}")
print(f"Merkezi fark - Analitik sonuc: {abs(Merkezi_fark1-analitik_sonuc2)} ")



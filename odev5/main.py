#kıdem ve maaş için regresyon uygulaması
import matplotlib.pyplot as plt
import pandas as pd
dataset = pd.read_csv('Kidem_ve_Maas_VeriSeti.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3,
random_state = 0)
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
plt.scatter(X_train, y_train, color = 'red')
plt.title('Kıdeme Göre Maaş Tahmini Regresyon Modeli')
plt.xlabel('Kıdem')
plt.ylabel('Maaş')
plt.show()
plt.scatter(X_train, y_train, color = 'red')
modelin_tahmin_ettigi_y = regressor.predict(X_train)
plt.scatter(X_train, modelin_tahmin_ettigi_y, color = 'blue')
plt.title('Kıdeme Göre Maaş Tahmini Regresyon Modeli')
plt.xlabel('Kıdem')
plt.ylabel('Maaş')
plt.show()
plt.scatter(X_train, y_train, color = 'red')
modelin_tahmin_ettigi_y = regressor.predict(X_train)
plt.plot(X_train, modelin_tahmin_ettigi_y, color = 'blue')
plt.title('Kıdeme Göre Maaş Tahmini Regresyon Modeli')
plt.xlabel('Kıdem')
plt.ylabel('Maaş')
plt.show()
print(3)

#evin boyutu ve ücreti ile ilgili vektörel hesaplama regresyon uygulaması
# analitik çözüm örneği
import numpy as np
import matplotlib.pyplot as plt
# veri setimizin yuklenmesi ve okunmasi
# sadece price ve size kolonlarini yukluyoruz.
# veri setimiz
data_set = np.loadtxt('Realestate.csv', delimiter=',', dtype=None,
usecols=(2, 5), skiprows=1)
# Sadece ilk 50 tane kayidi aliyoruz.
# Fiyatlar
prices = data_set[:50, 0] / 1000
# Buyuklukler
sizes = data_set[:50, 1]
# Ev Fiyatlari - Buyuklukleri Plot una Bakalim.
plt.plot(sizes, prices, 'ro', marker='+', markersize=10)
plt.xlabel('House Sizes (in feet2)')
plt.ylabel('House Prices (in 1000s of dollars)')
# plt.show()
# y = A + Bx dogrusunu cizdirebilmek icin
# Katsayilarin hesaplanmasi
# Bizim modelimize gore x'ler ev buyuklukleri
# y 'ler ev fiyatlarini temsil etmektedir.
# x -- size
# y -- price
total_y = sum(prices)
total_x = sum(sizes)
total_y_2 = sum(prices * prices)
total_x_2 = sum(sizes * sizes)
total_x_y = sum(prices * sizes)
A = ((total_y * total_x_2) - (total_x * total_x_y)) / ((50 * total_x_2) -
(total_x * total_x))
B = ((50 * total_x_y) - (total_x * total_y)) / ((50 * total_x_2) - (total_x
* total_x))
# y = A + B * x
x = sizes
y = A + B * x
plt.plot(x, y)
plt.show()
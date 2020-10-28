# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 14:13:05 2020
@author: utkuk
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# Vektör yaratma
x = np.array([1, 6, 2])
print(x)
y = np.array([1, 4, 3])
print(y)
# Fonksiyon hakkında yardım
#help(np.array)
#help(len)
# x+y, öncelikle boyutları uyuyor mu diye kontrol ederek
len(x)
len(y)
x+y
print(x+y)
print("="*10)

# Matris yaratımı
#help(np.matrix)
x = np.array([1, 2, 3, 4])
print(x)
x.shape = (2,2)
print(x.shape)
x = np.array([1, 2, 3, 4]).reshape(2,2)   # array'i 2x2 matrise ceviriyor
print(x)
# Matrislerde basit işlemler
x*x
print(x*x)
x*2
print(x*2)
x+2
print(x+2)
np.sqrt(x)
print(np.sqrt(x))     # kokunu aliyor
np.power(x, 1/3)
print(np.power(x,1/3))   # 1/3 kuvvetini alıyor
print("-40 satir---"*40)
# Normal dağılıma göre dağılmış rassal değişkenler yaratma

x = np.random.randn(500)
print(x)
y = np.random.normal(loc = 10, scale = 2,size = 500)
print("-40 satir---"*40)
print(y)
print("-40 satir---"*40)
print(np.corrcoef(x,y)) # İki vektör arasındaki korelasyon katsayısı

print(np.mean(x)) # Ortalama
print(np.mean(y)) # Ortalama
print(np.std(x)) # Standart sapma
print(np.std(y))
print(np.random.seed(12)) # Tohum
#help(np.random.seed())

#np.random.randn(5)



plt.ylabel('this is the y-axis')
plt.xlabel('this is the x-axis')
plt.title('ilk grafigin')

# Grafik çizme
x = np.random.randn(100)
y = np.random.randn(100)
plt.plot(x,y,'bo')
#plt.show()


# Sıralı vektör yaratma
x = np.arange(1, 10)
print(x)
#x = np.linspace(1, 100, num = 50)
#print(x)
xx = np.transpose(np.tile(x, (10,2))) # x'de yer alan ifadeyi alir her bir ifadeyi yanyana 10 kez yazar. sonra bitirir. "2" olarak belirtilen de bunu kac kez yapacagini göster.
print(xx)


a = np.array([0, 1, 2])
print(np.tile(a, 2))
print("="*20)
print(np.tile(a, (2, 2)))
print("="*20)
print(np.tile(a, (2, 1, 2)))
print("="*20)

y = x
yy = np.tile(y, (5,1)) ## x'deki seriyi yanyana yazmistik bu fonksiyon ayni seriyi alır alt alta 5 kez yazar.
print("kkk="*20)
print(x)
print("kkk="*20)
print(yy)
print("kkk="*20)
yy = np.transpose(np.tile(yy,(5,2)))

print(yy)
print("="*20)
yy = np.tile(y, (5,1))
print(yy)



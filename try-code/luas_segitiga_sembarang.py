import math

print("--- Program Menentukan Luas Segitiga Sembarang ---")
a = int(input('Masukkan panjang sisi pertama : '))
b = int(input('Masukkan panjang sisi kedua : '))
c = int(input('Masukkan panjang sisi ketiga : '))

s = (a + b + c) / 2
operation = s * (s - a) * (s - b) * (s - c)

print(f'\nLuas segitiga sembarang dengan panjang segitiga a = {a}, b = {b}, dan c = {c} adalah')
# Luas
print(f'Akar pangkat dua dari {int(operation)}')


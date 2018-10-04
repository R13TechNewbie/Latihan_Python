#!/usr/bin/python

a=int(input("Masukkan angka pertama : "))
b=int(input("Masukkan angka kedua : "))
tambah=str(a+b)
kurang=str(a-b)
kali=str(a*b)
bagi=str(a//b)
print("Hasil operasi aritmatika:")
print("Penjumlahan = " + tambah)
print("Pengurangan = " + kurang)
print("Perkalian = " + kali)
print("Pembagian = " + bagi)

skor = []

for i in range (5):
    nilaiSaatIni = int(input("Tolong masukkan nilai "+str(i+1)+" :" ))
    skor.append(nilaiSaatIni)
    
print(skor)
    


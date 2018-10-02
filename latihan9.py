#!/usr/bin/python

def fungsi():
	print("ayam")
	print("ayam")
	print("ayam")

fungsi()

def cetak_kalimat_seru(kata):
	print(kata+"!")

cetak_kalimat_seru("ayam")

def perkalian(x):
	print(2*x)

perkalian(3)

def perkalian_input(x,y):
	print(x*y)

perkalian_input(5,6)

print(perkalian(2))

def fungsi_return(a,b):
	if a>b:
		return a
	elif b>a:
		return b
	else:
		print("a sama dengan b")

hasil = fungsi_return(4,8)
print(hasil)

print(fungsi_return(4,8))

def pembagian(a,b):
	hasil=a//b
	return hasil
	print("ini tidak akan tercetak")

print(pembagian(15,5))

print(pembagian(15,5)*2)

# print(perkalian(5)*2)
# perintah diatas menimbulkan error

#!/usr/bin/python

words = ["Halloo","apa","kabar","semua?"]
counter = 0

while counter <  len(words):
	print(words[counter] + "!")
	counter += 1

words = ["Halloo", "apa", "kabar", "semua?"]
for kata in words:
	print(kata)

for kounter in range(10):
	print("aku bukan ayam")

gambar = 10

for g in range(gambar+1):
	print("p"*g)
	
for g in range(gambar+1,0,-1):
	print("p"*g)
	
for g in range(gambar,0,-1):
	print(" "*g)
	for h in range(1,gambar,+2):
		print("p"*h)
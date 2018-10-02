array = {
	"atas": [1,2,3],
	"kiri": [1,3,5],
	"kanan": [4,4,3],
	0: [1,2,3]
}

print(array["atas"])
print(array[0])
array[0]= [4,4,3]
print(array[0])
array[8]= [2,7]
print(array)
array[0]= 8
print(array[array[0]])
print(0 in array)
print("kay" in array)
print(array["bawah"])

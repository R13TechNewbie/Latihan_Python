def tesYield():
	i=0
	while i < 5:
		yield i
		i+=1

print(list(tesYield()))

def tesReturn():
	i=0
	while i < 5:
		return i
		print i
		i+=1

#print(list(tesReturn()))
#ini bakal error, soalnya int bukan list, gk bisa di iterasi
print(tesReturn())

def tesReturnFor():
	i=0
	for i in range(5):
		return i
		print i
		i+=1

#print(list(tesReturnFor()))
#ini juga bakal error, soalnya int bukan list, jadi gk bisa di iterasi
print(tesReturnFor())

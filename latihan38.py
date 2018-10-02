from itertools import count

for i in count(3):
	print(i)
	if i >= 11:
		break

for i in count(3,2):
	print(i)
	if i>=30:
		break

from itertools import cycle

counter=0
ayam="apostrof"
for i in cycle(ayam):
	counter+=1
	print(i)
	if counter >=9:
		break

from itertools import repeat

paww=["ayam","kambing","kucing"]
print(list(repeat("ayam",5)))
print(list(repeat(65,3)))
print(list(repeat(paww,3)))
nums = [55, 44, 33, 22, 11]

if all([i > 5 for i in nums]):
	print("semuanya lebih besar dari 5")

if any([i%2==0 for i in nums]):
	print("ada yang genap")

for i in enumerate(nums):
	print(i)

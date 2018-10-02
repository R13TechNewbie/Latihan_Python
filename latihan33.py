ayam = lambda x: x*3
print(ayam(15))

iterasi=[1,2,3,4,5]

print((lambda x: x*3)(iterasi))
hasil=list(map(lambda apake: apake + 5, iterasi))
print(hasil)
result=list(filter(lambda apaya: apaya == 5, iterasi))
print(result)

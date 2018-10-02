sets={1,2,3,8,9,4}
kataSets = set(["ayam","kambing","kucing"])
kosonganSets = set()

print(sets)
print(kataSets)
print(9 in sets)
print("curut" not in kataSets)
print(kosonganSets)

sets.add(14)
sets.remove(4)
print(sets)

pertama = {5,4,3,2,1}
kedua = {3,4,5,8,9}

print(pertama | kedua)
print(pertama & kedua)
print(pertama - kedua)
print(kedua - pertama)
print(pertama ^ kedua)

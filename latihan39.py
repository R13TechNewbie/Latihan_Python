from itertools import accumulate

nomer=list(accumulate(range(4)))
print(nomer)

from itertools import takewhile

ambil_yg_pas= list(takewhile(lambda a: a<=4, nomer))
print(ambil_yg_pas)

from itertools import chain

asaku=list(chain(ambil_yg_pas,[3,3,3]))
print(asaku)

from itertools import permutations,product

huruf=["G","H"]
print(list(product(huruf, range(2))))
print(list(permutations(huruf)))


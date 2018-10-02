def multiply(a,b):
	return a*b

x=5
y=12

perkalian=multiply
print(perkalian(x,y))

def dua_kali(fungsi,a,b):
	return fungsi(fungsi(a,b), fungsi(a,b))

print(dua_kali(multiply,5,12))

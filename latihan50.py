class ayam:
	def __init__(ini):
		ini._password = False
		
	@property
	def password(ini):
		return ini._password
		
	@password.setter
	def password(ini,masukan):
		if masukan:
			a = input("Masukkan password: ")
			if "ayambakar" == a:
				ini._password = masukan
			else:
				raise ValueError("Salah Password")
			
f = ayam()
print(f.password)
f.password = True
print(f.password)
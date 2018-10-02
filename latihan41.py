class awal:
	def suara(ini):
		print("bau")

class ayam(awal):
	def suara(ini):
		print("kukuruyuk")
		super().suara()

class kambing(awal):
	def suara(ini):
		print("mbee")

out=kambing()
out.suara()
ayam().suara()

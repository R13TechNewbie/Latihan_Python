def dekorasi(fungsi):
	print("="*15)
	fungsi()
	print("="*15)

def cetak():
	print("hallo minna")

cetakan=dekorasi(cetak)

@dekorasi
def lagi():
	print("yosh ganbarimasho")

import os
from DiceRoll import DiceRoll

class __init__:
	#This program shows welcome text in ASCII image form
    #This program works in linux
	
	def decor(func):
		#decoration function
		def wrap():
			terminal_height, terminal_width = os.popen("stty size", "r").read().split()
			termwidth = int(terminal_width)
			print("=" * termwidth)
			func()
			print("=" * termwidth)
		return wrap
		
	def welcome():
		#print ASCII image "WELCOME", or if the terminal window too small, just print "welcome" string
		terminal_height, terminal_width = os.popen("stty size", "r").read().split()
		termwidth = int(terminal_width)
		if termwidth >= 60:
			print("""
      __  __   _____   _      ___   ___   _____   ___ 
     |  ||  | |  ___> | |    / __> /   \ /     \ | __> 
     |      | |  ___> | |__ | (__  | | | | | | | | __> 
     |__/\__| |_____> |____| \___> \___/ |_|_|_| |___>
			
			""")
		else:
			print("WELCOME")
		
	decorated = decor(welcome)
	decorated()
	
	def menu():
		print("\nPilih opsi :")
		print(" 1. Dice Roll Program")
		print(" 2. kambing")
		print(" 3. kucing")
	
	menu()
	masukan = input("\nMasukkan nomor opsi: ")
	print("\n")
	try:
		pilihan = int(masukan)
	except ValueError:
		print("Masukkan angka, bukan huruf")
		raise SystemExit
		
	if pilihan == 1:
		DiceRoll()
	else:
		print("Error")
		
	
		
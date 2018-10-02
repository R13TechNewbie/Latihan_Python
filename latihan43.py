class Word(str): 
	'''Class for words, defining comparison based on word length.''' 

	def __new__(kelas, word): 
		# Note that we have to use __new__. This is because str is an immutable 
		# type, so we have to initialize it early (at creation) 
		if ' ' in word: 
			print("Value contains spaces. Truncating to first space.")
			word = word[:word.index(' ')] # Word is now all chars before first space 
		return str.__new__(kelas, word) 

	def __gt__(self, other): 
		return len(self) > len(other) 
	def __lt__(self, other): 
		return len(self) < len(other) 
	def __ge__(self, other): 
		return len(self) >= len(other) 
	def __le__(self, other): 
		return len(self) <= len(other)
	def lebihbesar(ini,lainnya):
		return len(ini) > len(lainnya)
		
a=input("Masukkan kata pertama: ")
b=input("Masukkan kata kedua: ")
print(Word.__gt__(a,b))
print(Word.lebihbesar(a,b))

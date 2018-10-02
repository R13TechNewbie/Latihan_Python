import sys

def ssh(address,port,user):
	#perintah untuk menyambungkan ssh
	print("ssh " + address + " -p " + port + " -l " + user)

address=input("Masukkan alamat ssh: ")
port=input("Masukkan port ssh: ")
user=input("Masukkan user ssh: ")

ssh(address,port,user)
print("Connecting..")
sys.cmd("sleep 1")
print("Connected\n")
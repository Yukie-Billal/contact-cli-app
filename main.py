import db
import os 
os.system("clear")

def header():
	print(f"\n\n{'Contact List':^40}")
	print('\n', f"{'-'*30:^40}", '\n')

def table_check():
	if db.check() == 0:
		db.create_tb()

def get_command():
	print("Daftar command : \n - Tampilkan (g) \n - Insert (i) \n - Update (u) \n - Delete (d) ")
	return input("\nPilih Command / Perintah ")

while True:
	header()
	table_check()
	command = get_command()

	if command in ['g','G']:
		db.get()
	elif command in ['i','I']:
		nama = input("Masukkan nama : ")
		email = input("Masukkan email : ")
		db.insert(nama,email)
	elif command in ['u','U']:
		id = int(input("Masukkan id contact : "))
		nama = input("Masukkan nama baru : ")
		email = input("Masukkan email baru : ")
		db.update(id,nama, email)
	elif command in ['d','D']:
		id = int(input("Masukkan id contact : "))
		db.delete(id)
	
	if input("\nLanjut ? (y/n) ") not in ['y',"Y",'']:
		break
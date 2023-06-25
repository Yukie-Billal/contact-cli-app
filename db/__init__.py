from . import connect

# print(connect.getDB)
db = connect.getDB()
cursor = connect.getCursor()

from .insert import insert as ins
from .table import table

def getContacts():
	cek = cursor.execute("SELECT * FROM contact")
	if cek > 0:
		contacts = cursor.fetchall()
	return contacts

def insert(nama,email):
	sql = ins(nama,email)
	try:
		cursor.execute(sql)
		db.commit()
	except Exception as e:
		db.rollback()
		return e

def create_tb () :
	sql = table
	try:
		cursor.execute(sql)
		db.close()
	except Exception as e:
		print(e)

def check():
	sql = "SHOW tables"
	return cursor.execute(sql)

def get():
	contacts = getContacts()
	print(f"\n{'Contact - List':^40}\n")
	print(f"{'-'*30:^40}")
	print(f"{'No':<3} {'Nama':<20} {'email':<20}")
	for contact in contacts:
		print(f"{contact[0]}. {' ':<1}{contact[1]:<20} {contact[2]:<20}")

def update(id,nama,email):
	sql = "UPDATE contact SET nama = '%s' , email = '%s' WHERE id = %d" % (nama,email,id)
	try:
		cursor.execute(sql)
		db.commit()
	except Exception as e:
		print(e)
		db.rollback()

def delete(id):
	sql = "DELETE FROM contact WHERE id = %d" % (id)

	try:
		cursor.execute(sql)
		db.commit()
	except Exception as e:
		db.rollback()
		raise e
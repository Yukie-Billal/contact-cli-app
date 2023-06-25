import pymysql.cursors 

# db = pymysql.connect('localhost','root','','')
db = pymysql.connect(host='localhost',
					user='root',
					password='',
					database='cli-app')

def getCursor() :
	return db.cursor()

def getDB() :
	return db
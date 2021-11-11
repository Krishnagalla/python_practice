import mysql.connector
from mysql.connector import connection
from mysql.connector.errors import Error

def sql_connection(host, username, password, db_name='Git'):
	connection = None
	try:
		connection = mysql.connector.connect(
			host = host,
			username = username,
			password = password,
			database = db_name,
		)
		return connection
	except Error as conn_error:
		print (f"unable to connect {conn_error}")

def create_db_table(conn, query):
	cursor = conn.cursor()
	try:
		c= cursor.execute(query)
	except Error as create_db_error:
		print(f"Failed to create DB {create_db_error}")

def fetch(conn, query):
	cursor = conn.cursor()

	try:
		cursor.execute(query)
		return cursor.fetchall()
	except Error as fetch_error:
		print (fetch_error)

def insert_values(conn,query ):
	cursor = conn.cursor()
	try:
		cursor.execute(query)
		#cursor.commit()
	except Error as e:
		print(e)



#create a connection
# connection = sql_connection(host='127.0.0.1', username='dev_user', password='Devuser@45')

# # check db
# db_check = fetch(connection, query= """SELECT SCHEMA_NAME
#   FROM INFORMATION_SCHEMA.SCHEMATA
#  WHERE SCHEMA_NAME = 'GIT'""")

# table_check = fetch(connection, query="""show tables""")

# index = 0

# for i in db_check:
# 	if(i[0] != 'git'):
# 		print (db_check)
# 		# create a new DB
# 		print ("Creating Database....")
# 		creat_db_query = """create database IF NOT EXISTs GIT"""
# 		execute_create_db = create_db_table(connection, creat_db_query)
# 		print("Database created successfully....")

# for table in table_check:
# 	if table[index] != 'user_config':
# 		print (table[index] + '==>' + table )
# 		create_table_query = """create table user_config (
# 								ID int primary key,
# 								username varchar(20),
# 								emailid varchar(50),
# 								role varchar(15),
# 								created date
# 							)"""
# 		print ("Creating table....")
# 		table_create = create_db_table(connection, query=create_table_query)
# 		print ("Table created successfully")
# 		index = index+1
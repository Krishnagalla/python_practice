import mysql.connector
from mysql.connector import Error
import pandas as pd
  
def db_connection(host_name, username, password, db ='mysql_python'):
	connection = None

	try:
		connection = mysql.connector.connect(
			host = host_name,
			user = username,
			password = password,
			database = db
		)
		return connection
	except Error as err:
		print (f'Unable to connect error {err}')

def create_new_db(connection, query):
	cursor = connection.cursor()
	try:
		cursor.execute(query)

	except Error as ce:
		print(f'Query error {ce}')

def execute_query(connection, query):
	cursor = connection.cursor()
	try:
		cursor.execute(query)
		connection.commit()
		print ("Query executed successfull")

	except Error as e:
		print (f'Execute query error {e}')

def insert_query_execute(connection, insert_query):
	cursor = connection.cursor()
	try:
		cursor.execute(insert_query)
		connection.commit()
	except Error as e:
		print (f'Error {e}')

def fetch(connection, read_query):
	cursor = connection.cursor()
	result = None
	try:
		cursor.execute(read_query)
		result = cursor.fetchall()
		return result
	except Error as read_query_error:
		print (f'Unable to fetch {read_query_error}')


host_name = 'localhost'
username = 'dev_user'
password = 'Devuser@45'
database = 'mysql_python'
connection = db_connection(host_name=host_name, username=username, password=password)

create_db_query = f'CREATE DATABASE IF NOT EXISTS {database}'
create_db = create_new_db(connection, query=create_db_query)

create_orders_table = """
	create table IF NOT EXISTS orders(
		order_id int primary key,
		customer_name varchar(40) not null,
		product_name varchar(20) not null,
		date_ordered date,
		quantity int,
		unit_price float,
		ph_num varchar(10));
"""
#execute_create_table_query = execute_query(connection, create_orders_table)
insert_query = """
	insert into orders values
		(107, 'Krishna', 'Laptop', '2018-06-01', 1, 800, '1234567890'),
		(108, 'Galla', 'Books', '2018-09-01', 2, 900, '9847484090'),
		(109, 'Galla Krishna', 'Mac Book', '2018-08-01', 1, 1000, '1234567899'),
		(110, 'GK', 'AirPods', '2019-06-01', 1, 800, '1234567898'),
		(111, 'G Krishna', 'Smartwatch', '2020-06-01', 1, 1800, '1233567890'),
		(112, 'Krishna Galla', 'Mobile', '2021-03-01', 1, 2800, '1233367890');
"""
#iq = insert_query_execute(connection, insert_query)

fetch_query = """
	select * from orders;
"""
read_query_result = fetch(connection, fetch_query)

# for value in read_query_result:
# 	print (value)

format_db = []

for result in read_query_result:
	result = list(result)
	format_db.append(result)
columns = ["order_id", "customer_name", "product_name", "date_ordered","quantity", "unit_price", "ph_num"]

dataframe = pd.DataFrame(format_db, columns=columns)
print(dataframe)
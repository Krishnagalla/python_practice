from sql import *
import os
import re as r
#db connection

# connection = sql_connection(host='localhost', username='dev_user', password='Devuser@45')
# print (connection)
folder_path = 'C:\\Users\\Galla Krishna\\Desktop\\Python Practice'
folder_name = input('Please enter the folder name: ')
username = input('Please enter your username: ')
emailid = input('Please your email id:')

emailregex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

while(emailid):
	if not r.fullmatch(emailregex, emailid):
		print ('Please enter valid email id....')
		emailid = input('Please your email id:')
	else:
		print('We are getting things done, please relax')
		break

print ('Processing started....')
folder = folder_path +'\\'+folder_name
url = 'https://github.com/Krishnagalla/python_practice.git'
try:
	if not os.path.isdir(folder):
		print (f'Creating folder...')
		os.mkdir(folder)
		print (f'{folder} created...')
	os.chdir(folder)
	print("\n")
	print (f'Updating git config...')
	config_username = os.system(f'git config --global user.name {username}')
	config_username = os.system(f'git config --global user.email {emailid}')
	print (f'Updated git config...')
	print('setting up...')
	os.system('git init')
	os.system(f'git remote add origin {url}')
	os.system('git pull origin main')
	print ('Thank You for being patience, your intial setup is done')

except Error as e:
	print(f'Unable to create folder: {e}')

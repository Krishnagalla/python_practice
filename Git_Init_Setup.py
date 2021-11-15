from sql import *
import os
import re as r

#db connection
con = sql_connection(host='localhost', username='dev_user', password='Devuser@45')

### Pre-Defined variables
folder_path = 'C:\\Users\\Galla Krishna\\Desktop\\Python Practice'
folder_name = input('Please enter the folder name: ')
username = input('Please enter your username: ')
emailid = input('Please your email id:')
role = input('Please enter ur designation (Sr Dev, Dev, Ass Dev, Support etc..) :')
folder = folder_path +'\\'+folder_name
url = 'https://github.com/Krishnagalla/python_practice.git'

### chekcks for input
while (username):
	if not username:
		username = input('Please enter your username: ')
	else:
		break

while emailid:
	if not emailid:
		emailid = input('Please your email id:')
	else:
		break

while(role):
	if not role:
		role = input('Please enter ur designation (Sr Dev, Dev, Ass Dev, Support etc..) :')
	else:
		break

while(emailid):
	if not r.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', emailid):
		print ('Please enter valid email id....')
		emailid = input('Please your email id:')
	else:
		print('We are getting things done, please relax')
		break

print ('Processing started....')


### Git operations start 
try:
	if not os.path.isdir(folder):
		print (f'Creating folder...')
		os.mkdir(folder)
		print (f'{folder} created...Please note this is ur git folder')
	os.chdir(folder)
	print (f'Updating git config...')

	config_username = os.system(f'git config --global user.name {username}')
	config_email = os.system(f'git config --global user.email {emailid}')

	if username and emailid:
		print ('Entered into If')
			
		insert_int_db_git = f"""insert into user_config (username, emailid, role, created) values (\'{username}\', \'{emailid}\', \'{role}\', sysdate())"""
		insert_values(con, query=insert_int_db_git)
	print (f'Updated git config...')

	print('setting up...')
	os.system('git init')
	os.system(f'git remote add origin {url}')
	os.system('git pull origin main')
	print ('Thank You for being patience, your intial setup is done')

except Error as e:
	print(f'Unable to create folder: {e}')

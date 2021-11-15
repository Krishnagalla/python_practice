import sql
import os
import re
import subprocess as sp
import datetime

dt = datetime.datetime.now().strftime('%Y%m%d_%H%M%S%f')

#git_directory = input('Please enter full directory path where changes are made :')
#if os.path.isdir(git_directory):
status = sp.getoutput('git status')
filename = f'C:\\Users\\Galla Krishna\\Desktop\\Log\\git_commit_{dt}.log'
git_file = open(filename, 'w')
git_file.writelines(status)
git_file.close()
git_file_read = open(filename, 'r')
modified_list = []
add_list = []
for line in git_file_read:
	if re.match("\s+modified:", line):
		search = re.search('(\s+)(modified:)(.*)', line)
		modified_list.append(search.group(3).lstrip())
	if re.match("\t+", line) and not re.match("\s+modified:", line):
		print (line)
		add_list.append(line.strip())
print ("Modified files :" + " " +', '.join(modified_list))
print ("New files :"+ " " + ', '.join(add_list))
modified_join = ', '.join(modified_list)
add_join = ', '.join(add_list)
username = sp.getoutput('git config user.name')

commit_ids = dict()
if  modified_join or add_join :
	user_ack = input('The above mentioned files will be commited, Please confirm (Y/N):')
	if user_ack.upper() == 'Y':
		if add_join:
			add = sp.getoutput(f'git add -A')
			print(add)
		if modified_join:
			comment = input('Please provide a commit comment :')
		if comment:
			try:
				comit = sp.getoutput(f'git commit -a -m {comment}')#git commit -a --author='Kri2 <>' -m 'Testing username commit'
				print(f"commit {comit}")
			except os.error as e:
				print(f"unable to comment {e}")
	else:
		exit(0)
print ('Please take a note of commit ids above')
print (modified_list)
print (add_list)
#else:
#    print('Please reenter the directory full path')
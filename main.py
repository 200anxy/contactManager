import hashlib
import pyinputplus as pyip
from getpass import getpass
print('''
NOTE : If the cell completes after you enter your username,
 that means that your name is not in the database.

''')
name = input('What is your name?\n')
name = name.lower()
passwdf = open('hello.txt','r')
readlines = passwdf.readlines()
i=-1
for row in readlines:
  i = i+1
  if row.find(name) != -1:
    name_row = row
    break

passwd = getpass("Please input your password: ")

passwd = passwd.encode('utf-8')
removeLen = len(name) + 3
hashcheck = readlines[i]
hashcheck = hashcheck[removeLen:]
passwdcheck = hashlib.sha256(passwd).hexdigest()
if hashcheck != passwdcheck:
  print('Invalid password. Please try again')
  exit()
else:
  print('Success!')




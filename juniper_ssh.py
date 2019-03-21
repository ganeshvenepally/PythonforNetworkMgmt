import paramiko
import time
import getpass
import os
import datetime

## 
#password = getpass.getpass('Enter Password: ')
host_file = open('hosts.txt','r')

for host in host_file:
	#print ('This output is from ' + host)
	ssh_client = paramiko.SSHClient()
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh_client.connect(host.strip(),22,'gunny','pass123')
	remote_connection = ssh_client.invoke_shell()

	stdin, stdout, stderr = ssh_client.exec_command('show system commit | match "09-29"')
	status = stdout.channel.exit_status_ready()
	if status == 0:
		mystring = stdout.read()
		fh = open('output.txt', 'a')
		print mystring
		fh.write(mystring)
		fh.close()

#!/usr/bin/python3

import paramiko
import os


sel = input ("Seleccione 1 Ejecutar comando o 2 para copiar fichero del remotehost: ")

if (sel == "1"):
	pkey = paramiko.RSAKey.from_private_key_file('/root/.ssh/fronterakey', password='bolson')
	trans = paramiko.Transport(('192.168.58.144', 22))
	trans.connect(username='root', pkey=pkey)
	ssh = paramiko.SSHClient()
	ssh._transport = trans
	comando = input ("Indica el comando a ejecutar: ")
	stdin, stdout, stderr = ssh.exec_command(comando)
	print(stdout.read().decode())
	del stdin, stdout, stderr
	trans.close()
	print ("ejecucion correcta")

elif (sel == "2"):
	pkey = paramiko.RSAKey.from_private_key_file('/root/.ssh/fronterakey', password='bolson')
	trans = paramiko.Transport(('192.168.58.144', 22))
	trans.connect(username='root', pkey=pkey)
	ssh = paramiko.SSHClient()
	ssh._transport = trans
	sftp = paramiko.SFTPClient.from_transport(trans)
	sftp.get(remotepath='/root/Juan.txt', localpath='/root/Juan.txt')
	trans.close()
	print ("copia realizada")
	os.system('ls -la /root | grep Juan.txt && cat /root/Juan.txt')
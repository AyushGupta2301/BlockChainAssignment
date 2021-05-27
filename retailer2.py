import socket
import time

s = socket.socket()
print('Press 1 to connect to the market')
t = input()
if(t=='1'):          
	port = 12345
	print('connecting to market...')
	time.sleep(2)
	s.connect(('127.0.0.1', port))
	print('connected to peer : (\'127.0.0.1\',{})'.format(port))
	while(1): 
		if(str(s.recv(1024))=="b'validate'"):
			print('recieved request for validation press 1 to validate, 0 to reject')
			t = input()
			if(t=='1'):
				s.send(b'yes')
				print("Sent validation accepted")
				break
			else:
				s.send(b'no')
				break


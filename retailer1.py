import socket
import time
import sys

sys.path.append(".\definitions")
from customer_def import customer
from retailer_def import retailer
from transaction_def import transaction
from product_def import product
from blockchain_def import blk_chain
from blockchain_def import block

s = socket.socket()
port = 12345
s.bind(('', port))
print('Network Established host :localhost, port id :',port)         

c = list()
while(1):
	print('Press 1 to add more connections, 0 to proceed')
	t = input()
	if(t=='1'):
		s.listen()   
		print ('Waiting for connection...')
		c1, addr = s.accept()
		c.append(c1)
		print('Connected with peer :',addr)
	else:
		break
retailer1 = retailer('retailer1')
for i in range(10):
	retailer1.add_prdct(product(i,100*i,12*i))
t = str(c[0].recv(1024))
pid = int(t[6:7])
qty = int(t[7:len(t)-1])
price = 0
if(t[:6]=="b'reqt"):
	print('customer requesting transaction (\'{}\',{}) press 1 to accept, 0 to reject'.format(pid,qty))
	t = input()
	if(t=='1'):
		c[0].send(b'Validation in process please wait')
		c[1].send(b'validate')
		if(str(c[1].recv(1024))=="b'yes'"):
			print("Recieved validation from retailer 1 processing the transaction")
			time.sleep(2)
			for i in range(retailer1.nop):
				if(pid == retailer1.prdct[i].id):
					price = qty*retailer1.prdct[i].price
					break
			sendp = 'yes'+str(price)
			c[0].send(bytes(sendp,'utf-8'))
			print('Transaction successful')
		else:
			c[0].send(b'no')
			print('retailer 1 rejected the validation, transaction cannot be processed\nSending remarks to customer...')
else:
	print(t)
c[0].close()
c[1].close()
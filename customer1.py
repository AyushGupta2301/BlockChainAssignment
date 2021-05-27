import socket
import sys
import time
import datetime

sys.path.append(".\definitions")
from customer_def import customer
from retailer_def import retailer
from transaction_def import transaction
from product_def import product
from blockchain_def import blk_chain
from blockchain_def import block

customer1 = customer('customer1',10000)
chain_c1 = blk_chain()
rec = None
tranc = 0

while(1):
	s = socket.socket()
	print('press 1 to buy products, 0 to view previous transactions')
	t = input()
	if(t=='1'):
		port = 12345
		print('connecting to market...')
		time.sleep(2)
		s.connect(('127.0.0.1', port))
		print('connected to peer : (\'127.0.0.1\',{})'.format(port))
		print('Enter the product id')
		pid = input()
		print('Enter the quanitiy required')
		qty = input()
		senddet = 'reqt'+str(pid)+str(qty) 
		s.send(bytes(senddet, 'utf-8'))
		x = str(s.recv(1024))
		print(x[2:len(x)-1])
		while(1):
			r = str(s.recv(1024))
			if(r[:5]=="b'yes"):
				print('Transaction successful')
				customer1.balance -= int(r[5:len(r)-1])
				ctime = datetime.datetime.now()
				transaction0 = transaction('customer1','retailer1',pid,qty,int(r[5:len(r)-1]),ctime)
				block0 = block(transaction0)
				if(tranc!=0):
					block0.prev = rec
				chain_c1.add_block(block0)
				rec = block0
				tranc += 1
				print('Disconnected') 
				break
			else:
				print('Validation failed, try again later')
				break
		s.close()
	else:
		chain_c1.print_transaction()
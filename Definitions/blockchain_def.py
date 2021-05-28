import sys

class block:
	def __init__(self,tra):
		self.id = tra.genhash()
		self.tran = tra
		self.prev = None

	def dis_transaction(self):
		print('customer : {}, retailer : {}, product : {}, quantity : {}, amount : {}, time : {}'.format(self.tran.cid,self.tran.rid,self.tran.pid,self.tran.qty,self.tran.amt,self.tran.time))

class blk_chain:
	def __init__(self):
		self.genblk = None
		self.lastblk = None

	def add_block(self,blk):
		if(blk.id == 'c0r000'):
			self.genblk = blk
			self.lastblk = blk
		else:
			self.lastblk = blk

	def print_transaction(self):
		printblk = self.lastblk
		while(printblk):
			printblk.dis_transaction()
			printblk = printblk.prev 		


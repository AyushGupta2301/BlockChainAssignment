import sys
import datetime

class transaction:
	def __init__(self,cus,ret,prdct,qty,amt,time):
		self.id = 0
		self.cid = cus
		self.rid = ret
		self.pid = prdct
		self.qty = qty
		self.amt = amt
		self.time = time

	def genhash(self):
		hashstr = ''
		hashstr += str(self.cid)[0]
		hashstr += str(self.cid)[len(str(self.cid))-1]
		hashstr += str(self.rid)[0]
		hashstr += str(self.rid)[len(str(self.rid))-1]
		hashstr += str(self.pid)
		hashstr += str(self.qty)
		return hashstr

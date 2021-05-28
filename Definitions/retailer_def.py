import sys

class retailer:
	def __init__(self,id):
		self.id = id
		self.prdct = list()
		self.nop = 0

	def add_prdct(self,prdct):
		self.prdct.append(prdct)
		self.nop += 1

	def product_list(self):
		for i in range(self.nop):
			print('product id : {}, price : {}, available quantity : {}'.format(self.prdct[i].id,self.prdct[i].price,self.prdct[i].qty))

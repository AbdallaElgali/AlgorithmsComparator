import sys
from DSA import *
from MinQP_UnorderedArray import MinPQ
		
class Transaction:
	def __init__(self, s):
		data = s.split()
		self.person = data[0]
		self.date   = data[1]
		self.sum    = float(data[2])
	
	def __lt__(self, other):
		return self.sum < other.sum
		
	def __repr__(self):
		return self.person.ljust(10) + "\t" + self.date + "\t" + str(self.sum)
		

pq = MinPQ()
M = int(sys.argv[1])

while not stdIsEmpty():
	line = stdReadLine()
	item = Transaction(line)
	pq.insert(item)
	if pq.size() > M:
		pq.delMin()

while not pq.isEmpty():
	print(pq.delMin())

from DSA import *

class MinPQ:
	def __init__(self, capacity=100):
		self.pq = objArray(capacity)	# pq[i] = ith element on pq
		self.N = 0						# number of elements on pq

	def isEmpty(self):
		return self.N == 0
	
	def insert(self,e):
		self.pq[self.N] = e
		self.N += 1
		
	def delMin(self):
		minPos = 0
		for i in range(self.N):
			if self.pq[i] < self.pq[minPos]:
				minPos = i
		self.N -= 1
		exch(self.pq, minPos, self.N)
		return self.pq[self.N]
		
	def size(self):
		return self.N
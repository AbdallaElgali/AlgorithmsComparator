import DSA

class SeparateChainingHashST:
	class Node:
		def __init__(self, key, val, next):
			self.key = key
			self.val = val
			self.next = next

		def __repr__(self):
			return str(self.key) + ":" + str(self.val) + "->" + str(self.next)
	
	def __init__(self):
		self.__M = 97
		self.__st = DSA.objArray(self.__M)

	def __hashIndex(self, key):
		return hash(key) % self.__M
		
	def get(self, key):
		i = self.__hashIndex(key)
		x = self.__st[i]
		while x != None:
			if key == x.key:
				return x.val
			x = x.next
		return None
		
	def put(self, key, val):
		i = self.__hashIndex(key)
		x = self.__st[i]
		while x != None:
			if key == x.key:
				x.val = val
				return
			x = x.next
		self.__st[i] = SeparateChainingHashST.Node(key, val, self.__st[i])
		
		
	def __repr__(self):
		return str(self.__st)


if __name__ == "__main__":
	st = SeparateChainingHashST()

	st.put("DSA",1)
	st.put("GPT",2)
	st.put("AIS",3)
	
	print(st)

	print(st.get("DSA"))
	print(st.get("AIS"))
	print(st.get("VIS"))
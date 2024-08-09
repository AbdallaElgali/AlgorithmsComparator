import DSA

class LinearProbingHashST:
	def __init__(self):
		self.__M = 30001
		self.__vals = DSA.objArray(self.__M)
		self.__keys = DSA.objArray(self.__M)

	def __hashIndex(self, key):
		return hash(key) % self.__M
		
	def get(self, key):
		i = self.__hashIndex(key)
		while self.__keys[i] != None:
			if key == self.__keys[i]:
				return self.__vals[i] 
			i = (i+1) % self.__M
		return None

	def put(self, key, val):
		i = self.__hashIndex(key)
		while self.__keys[i] != None:
			if key == self.__keys[i]:
				break
			i = (i+1) % self.__M
		self.__keys[i] = key
		self.__vals[i] = val


	def __repr__(self):
		s = ""
		for i in range(self.__M):
			s += str(i) + " : " + str(self.__keys[i]) + " = " + str(self.__vals[i])	+ "\n"
		return s
		


if __name__ == "__main__":
	st = LinearProbingHashST()

	st.put("DSA",1)
	st.put("GPT",2)
	st.put("AIS",3)
	
	print(st)

	print(st.get("DSA"))
	print(st.get("AIS"))
	print(st.get("VIS"))

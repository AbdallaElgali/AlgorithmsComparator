class bool:
	def __hash__(self):
		if value:
			return 1
		else:
			return 0

class int:
	def __hash__(self):
		value = self
		if value == -1:
			value = -2
		return value
		
class string:
	def __hash__(self):
		if not self:
			return 0 # empty
		value = ord(self[0]) << 7
		for char in self:
			value = c_mul(1000003, value) ^ ord(char)
		value = value ^ len(self)
		if value == -1:
			value = -2
		return value
		
M = 10

def hashIndex(key):
	return hash(key) % M		


print(hash(True))	
print(hashIndex(-1005))



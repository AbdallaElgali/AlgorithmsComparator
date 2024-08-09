import hashlib,sys

pw = sys.argv[1]
bpw = bytes(pw, 'utf-8')

m = hashlib.sha1(bpw)
print(m.hexdigest())

m = hashlib.sha256(bpw)
print(m.hexdigest())

import gzip
import binascii

f = gzip.open('data/train-images-idx3-ubyte.gz', 'rb')

magic = f.read(4)
print(magic)
x = int.from_bytes(magic, byteorder="big")
print(x)
f.close()
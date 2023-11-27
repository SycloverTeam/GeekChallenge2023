from pwn import *
from Crypto.Util.number import *
from hashlib import sha256
from itertools import product 
import string 

table = string.ascii_letters+string.digits
rec = remote('59.110.20.54', int(5526))

_ = rec.recvuntil(b'XXXX:')
tail,h = _[83:83+16],_[104:104+64] 
for head in product(table,repeat=4): 
    m = "".join(head)+tail.decode() 
    h_ = sha256(m.encode()) 
    if h_.hexdigest() == h.decode():
        print("".join(head)) 
        break
rec.sendline("".join(head).encode())
print(rec.recvall())
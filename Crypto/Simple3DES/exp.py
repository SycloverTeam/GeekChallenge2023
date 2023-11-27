from pwn import *
from Crypto.Util.number import *
from hashlib import sha256
from itertools import product 
import string 
key = b'340282366920938463444927863358058659840'
table = string.ascii_letters+string.digits
rec = remote('59.110.20.54', 23333) 
_ = rec.recvuntil(b'XXXX:')
'''
sha256(XXXX+duk9TfBbBkPtgm89) == 668113cd526a0998b14263b4a2f144ba435d11e7c497fd8da88cf23297cbaabd
Give me XXXX: abcd

'''
tail,h = _[12:28],_[33:97] 
for head in product(table,repeat=4): 
    m = "".join(head)+tail.decode() 
    h_ = sha256(m.encode()) 
    if h_.hexdigest() == h.decode():
        print('find!') 
        break
rec.sendline("".join(head).encode())
rec.sendlineafter(b'>',b'2') 
rec.sendlineafter(b'>',key) 
ct = rec.recvline()[1:-1]
rec.sendlineafter(b'>',b'1') 
rec.sendlineafter(b'>',ct) 
rec.sendlineafter(b'>',key)
pt = rec.recvline()[1:-1]
print(long_to_bytes(int(pt)))

rec.close()
# b'SYC{DES_1s_0ut_0f_t1me}\xe1\x92z${S\x08\x7fm'''


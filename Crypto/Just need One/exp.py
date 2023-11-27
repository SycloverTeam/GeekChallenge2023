from pwn import *
from Crypto.Util.number import *
from hashlib import sha256
from itertools import product 
import string  


table = string.ascii_letters+string.digits
rec = remote('59.110.20.54', int(2613)) 




_ = rec.recvuntil(b'XXXX:')
print(_)
tail,h = _[12:28],_[33:97] 
print(tail,h)
for head in product(table,repeat=4): 
    m = "".join(head)+tail.decode() 
    h_ = sha256(m.encode()) 
    if h_.hexdigest() == h.decode():
        print('find!') 
        break
rec.sendline("".join(head).encode())

rec.sendlineafter(b'>',str(int(2**32-1)).encode()) 

res = int(rec.recvline().decode()) 
ans = "" 
for _ in range(128): 
    ans+=str((res//((2**32-1)**_))%(2**32-1))+"," 
ans = ans[:-1]
rec.sendlineafter(b'>',ans.encode()) 
print(rec.recvline())

# b' Congrats! Your flag is: SYC{Alg0r1thm_1s_s0_S1mpl3!}\n'
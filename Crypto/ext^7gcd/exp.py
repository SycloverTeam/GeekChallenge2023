from sage.all import *
from pwn import *
from Crypto.Util.number import *
from hashlib import sha256
from itertools import product
import string

table = string.ascii_letters+string.digits
rec = remote('59.110.20.54', int(1789))
_ = rec.recvuntil(b'XXXX:')
tail,h = _[12:28],_[33:97]
for head in product(table,repeat=4):
    m = "".join(head)+tail.decode()
    h_ = sha256(m.encode())
    if h_.hexdigest() == h.decode():
        print('find!')
        break
rec.sendline("".join(head).encode())


try:
    while True:
        _ = rec.recvuntil(b"a6:").split(b'\n')[-2].split(b']') 
        ps, bts = eval(_[0][9:].decode()+']'), eval(_[1][3:-7].decode())
        print(ps)
        n = len(ps)
        S = 2**bts 
        X = Matrix(ZZ, n, n + 1) 
        for i in range(n):
            X[i, i + 1] = 1
        for i in range(n):
            X[i, 0] = S * ps[i] 

        L = X.LLL()

        M = L.row(n-1).list()[1:]
        if add(ps[i]*M[i] for i in range(n)) != 1:
            for i in range(n):
                M[i] = M[i]*(-1) 
        print(add(ps[i]*M[i] for i in range(n)))
        M = str(M)[1:-1].encode() 
        print(M)
        rec.sendline(M) 
except Exception:
    print(rec.recvall()) 


# SYC{N0t_s0_e4sy_3xtgCd}\n
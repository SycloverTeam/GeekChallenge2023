from pwn import *
from Crypto.Util.number import *
from hashlib import sha256
from itertools import product 
from gmpy2 import legendre as leg 

def s1(set): 
    p,a,b,c = set 
    if (b**2-4*a*c)%p !=0:
        return -leg(a,p) 
    else:
        return leg(a,p)*(p-1) 
    


key = b'FEFEFEFEFEFEFEFE'
table = string.ascii_letters+string.digits


rec = remote('59.110.20.54', 3042) 
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


m = rec.recvuntil(b'>').split(b'\n')
abc,p = m[-4].split(b' '),m[-3].split(b' ') 
print(abc)
print(p)
a,b,c,p = int(abc[0].decode()), int(abc[4].decode()), 1, int(p[2].decode())
set = (p,a,b,c) 
res = s1(set) 
print("rec = {}".format(res)) 


rec.sendline(str(res).encode()) 

try:
    while True:
        m = rec.recvuntil(b'>')
        m = rec.recvuntil(b'>').split(b'\n')
        abc,p = m[-4].split(b' '),m[-3].split(b' ') 
        print(abc)
        print(p)
        a,b,c,p = int(abc[0].decode()), int(abc[4].decode()), 1, int(p[2].decode())
        set = (p,a,b,c) 
        res = s1(set) 
        print("rec = {}".format(res)) 


        rec.sendline(str(res).encode()) 
except:
    rec.interactive()


# Congrats! Your flag is: b'SYC{G00d!_u_4r3_Qu33n_0f_Quadratic}'
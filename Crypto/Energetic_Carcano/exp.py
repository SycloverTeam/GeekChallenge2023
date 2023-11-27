from sage.all import * 
from pwn import *
from Crypto.Util.number import *
from hashlib import sha256
from itertools import product 
import string 
import gmpy2 as gp 

def solve(ct):
    ct = [i for i in ct] 
    for _ in range(len(ct)): 
        if ct[_]==")" and ct[_+1] == " ":
            ct[_] = ")," 
    ct = "".join(ct) 
    ct = eval(ct) 
    x,y = [ct[i][0] for i in range(cl)], [ct[i][1] for i in range(cl)] 
    k1=(x[0]-x[2])*((y[0]^2-x[0]^3)-(y[1]^2-x[1]^3))-(x[0]-x[1])*((y[0]^2-x[0]^3)-(y[2]^2-x[2]^3))
    k2=(x[0]-x[3])*((y[0]^2-x[0]^3)-(y[1]^2-x[1]^3))-(x[0]-x[1])*((y[0]^2-x[0]^3)-(y[3]^2-x[3]^3)) 
    p = int(gp.gcd(k1,k2) )
    ps = factor(p)
    p = ps[-1][0] 
    a = ((y[0]^2-x[0]^3)-(y[1]^2-x[1]^3))*gp.invert(x[0]-x[1],p)%p 
    b = (y[0]^2-x[0]^3-a*x[0])%p 
    return (a,b,p) 



cl = 4
key = b'FEFEFEFEFEFEFEFE'
table = string.ascii_letters+string.digits
rec = remote('59.110.20.54', int(8763)) 




_ = rec.recvuntil(b'XXXX:')

tail,h = _[12:28],_[33:97] 
for head in product(table,repeat=4): 
    m = "".join(head)+tail.decode() 
    h_ = sha256(m.encode()) 
    if h_.hexdigest() == h.decode():
        print('find!') 
        break
rec.sendline("".join(head).encode())


m = rec.recvuntil(b'>').split(b'\n') 
print(m)
if not m[-2].startswith(b'Give') and not m[-3].startswith(b'('):
    exit()
abp = chr(m[-2][-3]) 
pts = "["+m[-3].decode()+"]" 
print(abp,pts) 

set = solve(pts) 
a,b,p = set 
rec.sendline(str(eval(abp)).encode()) 


for _ in range(9):
    m = b"".join(rec.recvline() for _ in range(6)).split(b'\n') 
    print(m) 
    abp = chr(m[-2][-3])
    pts = "["+m[-3].decode()+"]" 
    set = solve(pts) 
    a,b,p = set 
    rec.sendlineafter(b">",str(eval(abp)).encode())  


print(rec.recvall())


# b" Good! Next challenge->\n\n||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n\nCongrats! Your flag is: b'SYC{ECC_M4ster}'\n"
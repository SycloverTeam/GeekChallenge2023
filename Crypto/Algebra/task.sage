#utf-8
#sage


import os
from Crypto.Util.number import *
from Crypto.Util.Padding import pad
from secret import flag,e
from functools import reduce

assert reduce(lambda x,y:x&y,[i^3 - 10*i^2 + 31*i - 30==0 for i in e])

LEN = 32
flag = pad(flag,36)

def LongArray(t:list):
    return [bytes_to_long(t[i]) for i in range(len(t))]

def BytesArray(t:list):
    return [long_to_bytes(t[i]) for i in range(len(t))]

def xor(a, b):
    return bytes([a[i%len(a)] ^^ b[i%len(b)] for i in range(max(len(a), len(b)))])

def ArrayXor(a:list,b:bytes):
    return [xor(a[i],b) for i in range(len(a))]

def scissors(flag:bytes):
    return [flag[i:i+len(flag)//3] for i in range(0, len(flag), len(flag)//3)]

def challenge(m: bytes, bits: int, level: int):
    p = getPrime(bits)
    M = random_matrix(Zmod(p), LEN).matrix_from_rows_and_columns(range(LEN), range(LEN-level))
    c = vector(GF(p), m) * M
    return {"p": p, "M": M.list(), "c": c.list()}

def groebner_challenge(m,e):
    p = getPrime(1024)
    s = sum(m)
    c = [pow(m[i],e[i],p) for i in range(3)]
    c.insert(0,s)
    c.insert(0,p)
    return c

key = os.urandom(LEN)
Get_key = challenge(key,256,0x10)

S_bytes = scissors(flag)
C_bytes = ArrayXor(S_bytes,key)
C_long  = LongArray(C_bytes)

groebner_challenge = groebner_challenge(C_long,e)

with open('keyTask.chall', 'w') as f:
    f.write(f"{Get_key}")

with open('groebnerTask.chall','w') as f:
    f.write(f"{groebner_challenge}")

















 


 





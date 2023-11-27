from pwn import *
from Crypto.Util.number import *
from functools import reduce
from cards import Heart, Spade, Club, Diamond
import gmpy2

def choose_card(num):
    x = (num>>5)%4
    if x == 0:
        return 'Heart_'+Heart[(num>>6)%13][15]
    if x%4 == 1:
        return 'Spade_'+Spade[(num>>6)%13][15]
    if x%4 == 2:
        return 'Diamond_'+Diamond[(num>>6)%13][15]
    else:
        return 'Club_'+Club[(num>>6)%13][15]

def attack(gift_list):
    diffs = [s1 - s0 for s0, s1 in zip(gift_list, gift_list[1:])]
    zeroes = [t2*t0 - t1*t1 for t0, t1, t2 in zip(diffs, diffs[1:], diffs[2:])]
    n = int(abs(reduce(gmpy2.gcd, zeroes)))
    m = (gift_list[2] - gift_list[1]) * inverse(gift_list[1] - gift_list[0], n) % n
    c = (gift_list[1] - gift_list[0]*m) % n
    return n, m, c

sh = remote("59.110.20.54","4953")
sh.recvuntil(b'input your option:')
sh.send(b'1\n')
data = sh.recvuntil(b'round:4')
crack_list = []

gift_matches = re.findall(r'gift: \[(.*?)\]', data.decode())
for gift_match in gift_matches:
    for num in gift_match.split(','):
        crack_list.append(int(num))
print(f'Crack List: {crack_list}')
lcg = []
res = []
n, m, c = attack(crack_list)
output = crack_list[-1]

for i in range(150):
    output = (output*m+c)%n
    lcg.append(output)
for num in lcg:
    data = choose_card(num)
    res.append(data)
res_t = [res[i:i+3] for i in range(0, len(res), 3)]
for datas in res_t:
    sh.recvuntil(b'Give me your guess: (example: Heart_1 Club_2 Diamond_3)\n')
    data = " ".join(datas)
    print(data)
    sh.send(data.encode()+b'\n')

sh.recvuntil(b'The flag is your reward!\n')
flag = sh.recvline().decode()
print(flag)
# SYC{lcg_a@@@@@ttack}
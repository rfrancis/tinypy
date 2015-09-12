#!/usr/bin/env python3

# vim:set ai sw=2 ts=2:

import readline
import textwrap
import sys
from threading import Thread
from telnetlib import Telnet

def handle_input(inf):
	while True:
		s=inf.read_until(b'\n',timeout=1)
		if len(s) > 0:
			for line in textwrap.wrap(s.decode('ascii'),79,subsequent_indent=' '):
				print(line)

host = sys.argv[1]
port = int(sys.argv[2])
tel = Telnet(host,port)
t=Thread(target=handle_input,args=(tel,))
t.start()

while True:
	try:
		s=input()
	except KeyboardInterrupt:
		print("!! Keyboard Interrupt ignored")
	else:
		if s[0] == '/':
			a = s[1:].split()
			exec("do_"+a[0]+"(a[1:])")
		else:
			if tel != None:
				s+="\n"
				tel.write(s.encode('ascii'))

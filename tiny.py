#!/usr/bin/env python3

import readline
from threading import Thread
from telnetlib import Telnet

tel = None

def handle_input(inf):
	while True:
		s=inf.read_until(b'\n',timeout=1)
		print(s.decode('ascii'),end='')

def do_help(args):
	print("I cannot currently help you with "+" ".join(args))

def do_connect(args):
	global tel
	host = args[0]
	port = int(args[1])
	tel = Telnet(host,port)
	t=Thread(target=handle_input,args=(tel,))
	t.start()

while True:
	s=input()
	if s[0] == '/':
		a = s[1:].split()
		exec("do_"+a[0]+"(a[1:])")
	else:
		if tel != None:
			s+="\n"
			tel.write(s.encode('ascii'))

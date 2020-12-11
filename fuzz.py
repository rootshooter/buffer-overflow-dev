#!/usr/bin/python
import optparse, sys, socket, time

parser = optparse.OptionParser('Example: python fuzz.py -t <target host> -p <target port> -c <command>')
parser.add_option('-t', dest='target', type='string', help='Enter a target host')
parser.add_option('-p', dest='port', type='int', help='Enter a target port')
parser.add_option('-c', dest='command', type='string', help='Enter a command')
(options, args) = parser.parse_args()
target = options.target #IP Address
port = options.port #Port Number
command = options.command # "COMMAND "

if (target == None) | (port == None):
	print(parser.usage)
	exit(0)

print('\n------------------------------------FUZZ----------------------------------------')
print('                              Author: @rootshooter')
print('                                 Version: 1.0')
print('--------------------------------------------------------------------------------')


payload = "A" * 100 #CHANGE AS NEEDED

while True :
	try:
		print('[+] Sending Payload')
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((target , port))
		s.send((command + payload))
		s.recv(1024)
		s.close()
		time.sleep(1)
		payload = payload + "A" * 100

	except:
		print('[+] Crash detected at %s bytes!\n' % str(len(payload)))
		sys.exit()










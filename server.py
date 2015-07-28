# Echo server program
import socket
from thread import start_new_thread

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 8000              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(10)

def clientthread(conn):

	while True:
		data = conn.recv(1024)
		if not data: 
			break
		print "Pregunta: ", data
		response = "Claro, callate"
		conn.send(response)

	conn.close()

while 1:
	conn, addr = s.accept()
	print 'Connected with ' + addr[0] + ':' + str(addr[1])
	start_new_thread(clientthread ,(conn,))
s.close()
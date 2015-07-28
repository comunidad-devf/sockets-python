# Echo client program
import socket

HOST = 'localhost'    # The remote host
PORT = 8000
ask = ''              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
ask = raw_input("Pregunta: ")
s.send(ask)
data = s.recv(1024)
s.close()
print 'Respuesta: ', repr(data)
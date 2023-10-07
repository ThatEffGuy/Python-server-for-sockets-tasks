import socket

s = socket.socket()
host = socket.gethostname()
port = 4444

a = input('enter 1st no:')
b = input('enter 2nd no:')
c = (a + ',' + b).encode()
print(c)

s.connect((host, port))
print('sending string {} to the server'. format(c.decode))
s.sendall(c)

data = s.recv(1024)
print (int(data))

s.close()
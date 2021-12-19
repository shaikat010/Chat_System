import socket


c = socket.socket()

#server will bind the port number and client will simply
#connect the port number together

c.connect(('localhost', 9999))
name = input("Enter your name")
query = input('what do you want to know?')

c.send(bytes(name, 'utf-8'))
#c.close()
c.send(bytes(query, 'utf-8'))
#c.send(bytes(query,'utf-8'))
print(c.recv(1024).decode())



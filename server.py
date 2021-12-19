import socket

s = socket.socket()

print('socket created')

#this is the server socket that accepts the port numbers

s.bind(('localhost', 9999))

#start listening to the client
#listneing for 3 clients
s.listen(3)

print('waiting for connection')

while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()
    #c.close()

    #query = c.recv((1024).decode())
    #print("Query received about: Potatoes")
    print('client connected with', addr,name)
    c.send(bytes('Hello ' + str(name) + ' welcome to Shaikat Server', 'utf-8'))
    #c.send(bytes("Thank you for making a query about " + str(query)))

    c.close()



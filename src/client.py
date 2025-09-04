import socket
#--------------------------------------------------
print("Answer by typing (1) for true, and with (0) for false. \n")
input01 = int(input("Socket is a way to send messages across a network. \n"))
input02 = int(input("The method bind(), Binds the socket to a specific host and port. \n"))
input03 = int(input("The Server program can accept a connection from any host by setting the host as empty. \n"))
input04 = int(input("After running the server program we built, your terminal will appear to hang. That’s because the server is blocked because .accept() method is blocking actions till a connection is requested. \n"))
input05 = int(input("socket.socket() method, returns a socket object whose methods implement the various socket system calls. Methods like: socket.accept(), socket.bind(), and more. \n"))
#--------------------------------------------------
arrayInputs = [input01, input02, input03, input04, input05]
byte_object = bytes(arrayInputs)
c = socket.socket()
c.connect(("localhost", 9999))
c.send(byte_object)
print(c.recv(1024).decode())




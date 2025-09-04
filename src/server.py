import socket

def checkGrade(intger_list):
    count = 0
    for x in intger_list:
        if x == 1:
            count = count + 1

    if count >= 3:
        return 1
    else:
        return 0



mySocket = socket.socket()
mySocket.bind(("localhost", 9999)) 
mySocket.listen(3)
while True:
    c, address = mySocket.accept()
    intger_list = list(c.recv(1024))
    if checkGrade(intger_list) == 1:
        c.send("Passed".encode())
    else:
        c.send("Failed".encode())
    c.close()



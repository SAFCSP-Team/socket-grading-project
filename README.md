# Socket Grading Project


### Objective

In this project, we will learn how to create Server-Client program using Socket.

### Problem   

Create a Server-Client program for taking an exam for a student, calculating his score, and then deciding if he passed or failed based on his scores.

### Implementation


**Client** 

- Test the student by asking multiple questions and taking the answers from the student as user input.
- Convert the student answers list from integers to bytes.
- Initiate the connection to the server program.
- Sends the student answers list to the Server program (REQUEST).
- Print the Server (RESPONSE).


**Server** 

- Sets up  listening socket.
- Receive the student answers list (REQUEST) as bytes.
- Convert the student answers list (REQUEST) from bytes to integer.
- Create a function that takes the student answers list, calculates the student score, and returns 1 if the  student has passed or 0 if the student has failed.
- If the student answers **3 or more** questions correctly he will **pass**, and **fails** otherwise.
- Send the (RESPONSE) to the client indicating either passed or failed.


### Test Case

- After running the server, run the client.
- Client console screen: 

```
Answer by typing (1) for true, and with (0) for false.
Socket is a way to send messages across a network
```
User input `1`
```
1
```
- Continue answering the questions:
```
The method bind(), Binds the socket to a specific host and port.
1
The Server program can accept a connection from any host by setting the host as empty.
1
After running the server program we built, your terminal will appear to hang. That’s because the server is blocked because .accept() method is blocking actions till a connection is requested.
1
socket.socket() method, returns a socket object whose methods implement the various socket system calls. Methods like: socket.accept(), socket.bind(), and more.
1
```
- Initiate the connection to the server
```
connection requested
```
- Print the Server program RESPONSE
```
Received b’passed’
```

### Final Output (the complete test case)

- After successfully running the program, here is the output
```
Answer by typing (1) for true, and with (0) for false.
Socket is a way to send messages across a network
1
The method bind(), Binds the socket to a specific host and port
1
The Server program can accept a connection from any host by setting the host as empty
1
After running the server program we built, your terminal will appear to hang. That’s because the server is blocked because .accept() method is blocking actions till a connection is requested.
1
socket.socket() method, returns a socket object whose methods implement the various socket system calls. Methods like: socket.accept(), socket.bind(), and more
1
connection requested
Received b’passed’
```




import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    operation = s.sendall(input("Please enter your operation: ").encode())
    n1 = s.sendall(input("Please enter the first number: ").encode())
    n2 = s.sendall(input("Please enter the second number: ").encode())
    data = s.recv(1024)

print('Received', repr(data))

# use while loop
# get by 16 byte
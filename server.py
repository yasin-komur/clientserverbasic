import socket

HOST = '127.0.0.1'
PORT = 65432

def operations(n1, n2, operation):
    n1, n2 = int(n1), int(n2)

    if operation == "add":
        return n1 + n2
    elif operation == "subtract":
        return n1 - n2
    elif operation == "multiply":
        return n1 * n2
    elif operation == "divide":
        return n1 / n2
    else:
        print("We are not that good!")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        op = ""
        while True:
            data = conn.recv(1024)
            op += data.decode() + " "
            if not data:
                break
            conn.sendall(data)
        print(operations(op.split()[1], op.split()[2], op.split()[0]))

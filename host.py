import socket
s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host, port))
name = input("Enter the username")
s.listen()
print("waiting for client to connect....")
conn, addr = s.accept()
print("recieved succesfully")
# CONNECTION DONE


s_name = conn.recv(1024)
s_name = s_name.decode()
print(f"{s_name} has joined the chat room")
conn.send(name.encode())

# MESSAGE

while True:
    message = input("Enter the text:")
    conn.send(message.encode())
    text = conn.recv(1024)
    text.decode()

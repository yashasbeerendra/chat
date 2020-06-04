import socket
import time
s = socket.socket()
print("Initialising....")
host = input("Enter the host name")
port = 8080
name = input("Enter your username")
s.connect((host, port))
print(f"connected succesfully")
s.send(name.encode())
s_name = s.recv(1024)
s_name.decode()
print(f"{s_name} has joined the chat room")
while True:
    message = s.recv(1024)
    message.decode()
    text = input("enter the text:")
    s.send(text.encode())

# server.py
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)

print("Server is listening...")
conn, addr = server_socket.accept()
print(f"Connected by {addr}")

data = conn.recv(1024)
print("Received:", data.decode())

conn.sendall("Hello from server!".encode())
conn.close()
# more complex program needed
# iam unable to do my mern seires continuously help me god . i am lacking my consistency 
#  in day i need to do coding 
# the day dint went well as planned

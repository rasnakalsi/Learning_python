import socket
server_addr=input("What Server do you want to connect to??")
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect((server_addr,80))
sock.send(b"GET / HTTP/1.1 \r\n Host:"+bytes(server_addr,"utf-8")+b"\r\nConnection:close\r\n\r\n")
reply=sock.recv(10000)
sock.shutdown(socket.SHUT_RDWR)
sock.close()
print(repr(reply))

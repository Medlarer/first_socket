import socket
ip_port = ("127.0.0.1",9000)
data_len = 1024
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect_ex(ip_port)
s.send('hello qiu'.encode('utf-8'))
feedback = s.recv(data_len)
print(feedback.decode("utf-8"))
s.close()

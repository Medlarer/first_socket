import socket
ip_port = ("127.0.0.1",9000)
data_len = 1024
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect_ex(ip_port)
while True:
    msg = input(">>:").strip()
    if not msg:
        continue
    s.send(msg.encode('utf-8'))
    feedback = s.recv(data_len)
    print(feedback.decode("utf-8"))
s.close()

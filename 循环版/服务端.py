import socket
ip_port = ('127.0.0.1',9000)
data_len = 1024
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(ip_port)
s.listen(5)

while True:
    conn,addr = s.accept()
    print('接到来自%s的通信' %addr[0])
    while True:
        msg = conn.recv(data_len)
        print(msg,type(msg))
        conn.send(msg.upper())
    conn.close()
s.close()
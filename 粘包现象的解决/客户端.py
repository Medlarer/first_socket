import socket
re_len = 1024
ip_port = ("127.0.0.1",8080)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
res = s.connect_ex(ip_port)

while True:
    msg = input(">>:").strip()
    if len(msg) == 0:continue
    if msg == "quit" or msg == "exit":break
    s.send(msg.encode("utf-8"))
    act_res = s.recv(re_len)
    print(act_res.decode("gbk"),end="")
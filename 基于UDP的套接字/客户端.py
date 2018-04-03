import socket
ip_port = ("127.0.0.1",9000)
re_len = 1024
udp_server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    msg = input(">>:").strip()
    if not msg:
        continue
    udp_server.sendto(msg.encode("utf-8"),ip_port)
    back_msg,addr = udp_server.recvfrom(re_len)
    print(back_msg.decode("utf-8"),addr)

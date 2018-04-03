from socket import *
import struct,json

ip_port = ("127.0.0.1",8080)
client = socket(AF_INET,SOCK_STREAM)
client.connect(ip_port)
while True:
    cmd = input(">>:").strip()
    if not cmd:continue
    client.send(cmd.encode("utf-8"))

    head = client.recv(4)
    head_json_len = struct.unpack('i',head)[0]
    head_json = json.loads(client.recv(head_json_len).decode("utf-8"))
    data_len = head_json.get("data_size")

    recv_size = 0
    recv_data = b''
    while recv_size < data_len:
        recv_data += client.recv(1024)
        recv_size += len(recv_data)
    print(recv_data.decode("gbk"))


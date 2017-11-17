# _*_ coding:utf8 _*_

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.10.100.217', 10001))

while True:
    data = input(">")
    if not data:
        break

    s.send(data)
    if data == "exit":
        break
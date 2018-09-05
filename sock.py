import socket
import sys
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 9930)

while True:
    sent = sock.sendto(b'%d;0;0;1;' % random.randint(0, 1), server_address)

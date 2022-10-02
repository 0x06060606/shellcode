import os, sys,socket

try:
    iw4xServer   = ("47.206.201.17",28960)
    UDPSocket = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
    UDPSocket.sendto(b'\xff\xff\xff\xffdisconnect\n',iw4xServer)
    Buffer = UDPSocket.recvfrom(8096)[0]
    print(Buffer)
finally:
    UDPSocket.close()
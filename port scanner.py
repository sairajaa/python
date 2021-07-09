import socket
import sys

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
hostname = input("enter the hostname:")
ip = socket.gethostbyname(hostname)

port = 80

try:
    result = s.connect_ex((ip,port))
    if result == 0:
        print ("port {}: open".format(port))
    else:
        print ("port {}: closed".format(port))
    s.close
except socket.error:
    print("error")
 
 

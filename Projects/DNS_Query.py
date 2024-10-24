import socket
import time

def query(ip):
    output = socket.AddressInfo(ip)
    return output

print("Starting DNS query for 10.0.0.0/8 network...")


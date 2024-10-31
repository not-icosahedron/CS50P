import socket

file = open("dns_query.csv", "w")

print("starting DNS query for 10.0.0.0/8...")

file.write("IP Address,Hostname\n")
file.flush()

# Open the file using 'with' to ensure it's properly closed
#with open("dns_query.txt", "a") as file:


def print_reverse_dns(ip, file):
    try:
        output =str(ip + ','  + socket.gethostbyaddr(ip)[0])
        output = output.upper()
        print(output)
        file.write(output + "\n")
        file.flush()
    except Exception:
        #output = str(ip) + " | No Response..."
        #print(output)
        #file.write(output + '\n')
        #file.flush()
        return ip, print(str(ip) + " | " + "No Response...")

def generate_ips():
    for i in range(255):
        i += 1
        return i


for ip2 in range(0,256):
    for ip3 in range(0,256):
        for ip in range(1,256):
            query = '10.' + str(ip2) + '.' + str(ip3) + '.' + str(ip)
            print_reverse_dns(query, file)

file.close()
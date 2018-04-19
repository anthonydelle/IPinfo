from modules.IPinfo import IPinfo
import socket

while True:
    userinput = input("Please supply an IP address or press Enter to use your current IP")

    if userinput:
        try:
            socket.inet_aton(userinput)
            break
        except socket.error:
            print("Invalid IP")

a = IPinfo(userinput)

print(a.allinfo())

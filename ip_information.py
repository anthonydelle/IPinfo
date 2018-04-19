from modules.ipinfo import IPinfo
import socket
import pprint

userinput = ""

while True:
    userinput = input("Please supply an IP address \
or press c to use your current IP")
    if userinput == "c":
        userinput = ""
        break
    else:
        try:
            socket.inet_aton(userinput)
            break
        except socket.error:
            print("Invalid IP")

a = IPinfo(userinput)

pprint.pprint(a.allinfo())

#!/usr/bin/python2.7
import socket
import time

host = '34.107.86.157'
port = 31450

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

#-------------------------q1----------------------------
q1 = s.recv(1024)
q1 += s.recv(1024)
print(q1)

#grab value in << val >>
splitBanner = q1.split(" ")
val = splitBanner[5].replace('<<', '').replace('>>', '')
intVal = int(val)

#convert int to hex
hexVal = hex(intVal)

print("[+] test: " + hexVal)
s.send(hexVal + '\n')

q2 = s.recv(1024)

print(q2)

#-------------------------q2----------------------------
#grab value in << val >>
splitBanner = q2.split(" ")
val = splitBanner[5].replace('<<', '').replace('>>', '')

#convert hex to ASCII
asciiVal = val.decode("hex")

print("[+] test: " + asciiVal)
s.send(asciiVal + '\n') 

q3 = s.recv(1024)

print(q3)

#-------------------------q3----------------------------
#grab value in << val >>
splitBanner = q3.split(" ")
val = splitBanner[5:25]
val[0] = val[0].replace('<<', '')
val[-1] = val[-1].replace('>>', '')

#convert octal to ASCII
convASCII = [chr(int(i, 8)) for i in val]
asciiVal = ''.join(convASCII)

print("[+] test: " + asciiVal)
s.send(asciiVal + '\n')   

flag = s.recv(1024)

print(flag)

s.close()


#!/usr/bin/env python3
import socket
import os
import fnmatch
import python-gnupg

def main():

    print('Initialising setup')
    netsetup()
    clientkey()

def netsetup():
    HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
    PORT = 64206        # Port to listen on (non-privileged ports are > 1023)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print("Request from ", addr)
            while true:
                data = conn.recv(1024)
                if not data:
                    break




def clientkey():

    print('Validating client ' + ' with key: ' data)
    licensekey = input()
    license = open("./license.txt","w")
    license.write(licensekey)

def keyvalidate():

    netsetup()
    socket.send(licensekey.encode())
    serverreply = socket.recv(1024)



if __name__ == '__main__':
    main()

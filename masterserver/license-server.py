#!/usr/bin/env python3
import socket
import os
import fnmatch
import time

validated = false
data = ''

def main():

    print('Initialising setup')
    netsetup()
    clientkey()
    time.sleep(10000)
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
                validated = keyvalidate(data.decode())
                    if validated = true
                    conn.send("4321")
                else:
                if not data:
                    print("Net setup failed to receive incoming data")
                    break


def clientkey():

    print('Validating client ' + ' with key: ' data)
    licensekey = input()
    license = open("./license.txt","w")
    license.write(licensekey)

def keyvalidate(data):

    if data = '1234'
        return true
    else
        return false


if __name__ == '__main__':
    main()

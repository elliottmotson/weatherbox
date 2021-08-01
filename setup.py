#!/usr/bin/env python3
import socket
import os
import fnmatch


def main():

    print('Initialising setup')

    if haskey = false:

        for f_name in os.listdir('./'):
            if f_name.endswith('license.txt'):
                print("Licence file exists.")
                license = open("./license.txt" , "a")
                licensekey = license.read()
                print("LICENSE KEY - " + license)
                haskey = true
            else
                print("ERROR 0001: NO LICENCE FILE")

    else:
        keyvalidate()


def keyinput():

    print('Enter activation key: ')
    licensekey = input()
    license = open("./license.txt","w")
    license.write(licensekey)

def keyvalidate():

    netsetup()
    socket.send(licensekey.encode())
    serverreply = socket.recv(1024)


def netsetup():
    HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
    PORT = 64206        # Port to listen on (non-privileged ports are > 1023)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print("Connected to: ", addr)
            while true:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)

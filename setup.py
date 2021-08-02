#!/usr/bin/env python3
import socket
import os
import fnmatch
import time
import sys

def main():

    print('Initialising box setup')


    netsetup()
    print("NETWORKING COMPLETE - GREAT SUCCESS!")
    time.sleep(10000)


def keyinput():

    print('Enter activation key: ')
    licensekey = input()
    license = open("./license.txt","w")
    license.write(licensekey)

def connectremote():

    HOST = socket.gethostname()
    PORT = 4206
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    incoming = s.recv(1024)
    print("Connected master server: ", HOST)
    print("MESSAGE FROM LICENSING SERVER: " + incoming.decode("utf-8"))


<<<<<<< Updated upstream
def netsetup():
    HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
    PORT = 64206        # Port to listen on (non-privileged ports are > 1023)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print("Connected master server: ", addr)
            while true:
                print("Sending license key")
                conn.send("1234")
                data = conn.recv(1024)
                if data.decode() = "4321"
                    print("SERVER REPLY SUCCESSFUL. LICENSING COMPLETE")
                    return true
                if not data:
                    return false

=======
>>>>>>> Stashed changes
if __name__ == '__main__':
    main()

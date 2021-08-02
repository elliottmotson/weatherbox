#!/usr/bin/env python3
import socket
import os
import fnmatch
import time

validated = False
data = ''


def main():

    print('Initialising license server setup')
    launchremote()
    clientkey()
    time.sleep(10000)


def launchremote():

    HOST = socket.gethostname()
    PORT = 4206
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(10)
    print("LISTENING ON: ", PORT)

    while True:
        clientsocket, address = s.accept()
        print("CONNECTION TO POSSIBLE CLIENT ESTABLISHED")
        print("Verifying...")
        clientsocket.send(bytes("4321", "utf-8"))
        print("Sent activation reply to client ", address, ": 4321")


def clientkey():
    print('Validating client ' + ' with key: ' + data)
    licensekey = input()
    license = open("./license.txt", "w")
    license.write(licensekey)


def keyvalidate(data):

    if data.decode("utf-8") == '1234':
        return True
    else:
        return False


if __name__ == '__main__':
    main()

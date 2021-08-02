#!/usr/bin/env python3
import socket
import os
import fnmatch
import time
import sys


def main():

    print('Initialising box setup')

    connectremote()
    print("NETWORKING COMPLETE - GREAT SUCCESS!")
    time.sleep(10000)


def keyinput():

    print('Enter activation key: ')
    licensekey = input()
    license = open("./license.txt", "w")
    license.write(licensekey)


def connectremote():

    HOST = socket.gethostname()
    PORT = 4206
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    while True:
        incoming = s.recv(1024)
        print(incoming.decode("utf-8"))


if __name__ == '__main__':
    main()

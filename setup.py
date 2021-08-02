#!/usr/bin/env python3
import socket
import os
import fnmatch
import time


activated = False


def main():

    print('Initialising box setup')
    print("Validating box with master server...")

    if validated():
        print("NETWORKING COMPLETE - GREAT SUCCESS!")
    else:
        print("Unable to validate. Retrying...")

    input()


def keyinput():

    print('Enter activation key: ')
    licensekey = input()
    license = open("./license.txt", "w")
    license.write(licensekey)
    time.sleep(100)


def validated():

    HOST = socket.gethostname()
    PORT = 4206
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    while activated is False:
        print("Socket running")
        incoming = s.recv(1024)
        incoming = incoming.decode("utf-8")
        print("Message received" + incoming)
        if incoming == "4321":
            print("ACTIVATION KEY: " + incoming)
            print("ACTIVATION KEY CORRECT.")
            return True
        else:
            print("CONNECTION ERROR")
            break


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
import socket
<<<<<<< HEAD
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
=======
import os
import fnmatch
import time

def main():

    print('Initialising setup')
    time.sleep(10000)
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

    elif netsetup() = true:
        print("NETWORKING COMPLETE - GREAT SUCCESS!")

>>>>>>> moisturesensor


def keyinput():

    print('Enter activation key: ')
    licensekey = input()
<<<<<<< HEAD
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
=======
    license = open("./license.txt","w")
    license.write(licensekey)




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
>>>>>>> moisturesensor

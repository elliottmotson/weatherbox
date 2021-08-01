#!/usr/bin/env python3
import socket
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



def keyinput():

    print('Enter activation key: ')
    licensekey = input()
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

if __name__ == '__main__':
    main()

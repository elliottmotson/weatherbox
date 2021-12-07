#!/usr/bin/env python3
import socket
import os

activated = False


def main():

    print('Initialising box setup')
    print("Validating box with master server...")
    if masterconnect():
        print("NETWORKING COMPLETE - GREAT SUCCESS!")
    else:
        print("Unable to contact master server. Activate offline?")
        print("[1] Yes")
        print("[2] No")
        txtinput = input()
        if txtinput == "1":
            print('Please enter license key filename in current directory xxxxxxx.wb')
            activateoffine()
        else:
            print("Trying auto setup again...")
            main()
    print("Starting Sensor Engine...")
    sensorboot()
    print("Waiting for instructions...")
    input()


def sensorboot():
    os.system('python3 C:/weatherbox/sensorengine.py')
    print("Sensor Engine Started")


def validatekey(key):

    print('Fetched activation key from master server: ' + key)
    print('Validating key with public master...')


def masterconnect():

    if trynet():
        try:
            HOST = socket.gethostname()
            PORT = 4206
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((HOST, PORT))
            print("Contacting master server")
            while activated is False:
                incoming = s.recv(1024)
                incoming = incoming.decode("utf-8")
                print("Master Server reply: " + incoming)
                validatekey(incoming)
                if incoming == "LICENSEKEY":
                    print("ACTIVATION KEY: " + incoming)
                    return True
                else:
                    print("CONNECTION ERROR")
                    main()
                    break
        except ConnectionRefusedError:
            print("ERROR: ConnectionRefusedError")
            print(
                "Client port may be busy or master server unreachable Are two instances running?")
            return False
    else:
        print("NETWORK CONNECTION ERROR")


def trynet():
    response = os.system("ping " + "8.8.8.8")
    if response == 1:
        return False
    else:
        print("CAN REACH EXTERNAL INTERNET.")
        return True


def activateoffine():
    licensekey = input()
    license = open("/" + licensekey, "r")
    contents = license.read()
    if contents == "LICENSEKEY":
        print("PRODUCT ACTIVATED - WELCOME!")
        return True
    else:
        print("License file error, try again?")
        print("1. Yes")
        print("2. BACK TO MAIN")
        txtinput = input()
        if txtinput == "1":
            activateoffine()
        elif txtinput == "2":
            main()
        else:
            print("Invalid option, returning to main anyway...")
            main()


if __name__ == '__main__':
    main()

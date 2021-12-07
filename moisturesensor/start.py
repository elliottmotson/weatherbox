#!/usr/bin/env python3
import socket
import json
import time


def main():
    print("Initialising hub connection...")
    if hubconnect():
        senddata(parsesettings())
        print("Hub connected")
        input()
    else:
        print("No connection to hub, retrtying...")
        time.sleep(1)
        main()
    print("Waiting for instruction.")
    input()


def hubconnect():
    HOST = socket.gethostname()
    PORT = 6420
    data = ("HW-390")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(2)
    print("LISTENING ON: ", PORT)
    while True:
        clientsocket, address = s.accept()
        if clientsocket is not None:
            print("CONNECTION TO BOX ESTABLISHED")
            print("Sending data...")
            clientsocket.send(bytes(data, "utf-8"))
            print("Sent data to box @ ", address, ": ", data)
            return True
        else:
            print("Cannot connect to hub")
            time.sleep(1)
            continue


def recvdata():
    HOST = socket.gethostname()
    PORT = 420
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    while True:
        incoming = s.recv(1024)
        incoming = incoming.decode("utf-8")
        return incoming


def senddata(data):
    HOST = socket.gethostname()
    PORT = 420
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    print("LISTENING ON: ", PORT)
    while True:
        clientsocket, address = s.accept()
        print("CONNECTION TO BOX ESTABLISHED")
        print("Sending data...")
        clientsocket.send(bytes(data, "utf-8"))
        print("Sent data to box @ ", address, ": ", data)
    try:
        HOST = socket.gethostname()
        PORT = 420
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        while True:
            incoming = s.recv(1024)
            incoming = incoming.decode("utf-8")
            return incoming
    except ConnectionRefusedError:
        print("ERROR: ConnectionRefusedError")
        print("Client port may be busy or server unreachable")
        print("Are two instances running?")
        return False


def parsesettings():
    file = open('C:/weatherbox/moisturesensor/settings.json')
    data = json.load(file)
    print(data)
    file.close()
    return data


if __name__ == '__main__':
    main()

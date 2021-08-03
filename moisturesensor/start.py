#!/usr/bin/env python3
import socket


def main():
    print("Boot successful")
    print("Initialising...")
    senddata()
    input()


def senddata():

    data = 'HW-390'
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
        print(
            "Client port may be busy or master server unreachable Are two instances running?")
        return False


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
import socket
import threading


def main():
    init()
    #listenthread = threading.Thread(target=sensorlisten)
    #listenthread.start()
    data = sensorlisten()
    print(data)
    input()


def init():
    print("Initialising")
    settings = readsettings()


def readsettings():
    print("Reading settings")


def sensorlisten():
    listen = True
    HOST = "localhost"
    PORT = 6420
    print(HOST)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    print("Contacting sensor")
    while listen is True:
        incoming = s.recv(1024)
        print("SENSOR CONNECTED: " + incoming.decode("utf-8"))
        data = incoming.decode("utf-8")
        if data is not None:
            return data
        else:
            continue
    else:
        return False


if __name__ == '__main__':
    main()

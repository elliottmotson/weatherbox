#!/usr/bin/env python3
import socket
import json
import time

sensor = {
  "ID": "",
  "name": "",
  "type": "",
}

connected = False


def setup():
    print("Sensor Engine Started")
    print("SENSOR INIT...")
    print("MENU SETTINGS")
    print("[1] Activate Sensor Listening")
    userinput = input()
    if userinput == 1:
        sensorlisten()
    else:
        print("Invalid input, restarting...")
        main()


def main():
    while identifysensor(sensorlisten()) is False:
        print("Retrying connection with box in 1 second...")
        time.sleep(1)
    input()


def readsettings():
    print("Reading settings")


def sensorlisten():
    try:
        HOST = socket.gethostname()
        PORT = 420
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        print("Contacting sensor")
        while True:
            incoming = s.recv(1024)
            incoming = incoming.decode("utf-8")
            print("SENSOR CONNECTED SUCCESFULLY: " + incoming)
            return incoming
    except ConnectionRefusedError:
        print("ERROR: ConnectionRefusedError")
        print(
            "Client port may be busy or master server unreachable Are two instances running?")
        return False


def identifysensor(sensorname):
    if sensorname == "HW-390":
        sensor = {
          "ID": "1",
          "name": "HW-390",
          "type": "moisture",
        }
        return True
    else:
        return False


if __name__ == '__main__':
    main()

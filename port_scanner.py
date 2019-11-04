#!/usr/bin/python

''' port scanner made in python3
    Author: k0mmo
    Version: 1.0

    requirments to use:
    must pip install termcolor please use the command below.
  _____________________________________________________________

    pip3 install termcolor
  _____________________________________________________________
'''

import socket
from termcolor import colored
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #makes a socket IPv 4 connetion using tcp packets
socket.setdefaulttimeout(2) # times out instads of hanging

def menu():
    print(" ")
    print("____________________________________\n")
    print(colored("Port scanner", 'yellow'))
    print(" ")
    print("Version: " + colored(str("1.0"), 'cyan'))
    print("____________________________________\n")
    print(colored("please make a selection:", 'yellow'))
    print(" ")
    option = print("1.) Single port scan\n")
    option = print("2.) Scan all ports\n")
    option = print("3.) Exit\n")
    choice = input(">>> ")
    if choice == ('1'): # performs a single ip search
            single_scan()
    elif choice == ('2'): # performs a serach of all the ports
        print(" ")
        print(colored("***** Caution this scan can take a long time to complete. *****", 'red'))
        print("would you like to continue? y or n")
        user_choice = input(">>> ")
        if user_choice == ('y'):
            Scan_all()
        elif user_choice == ('n'):
            start()
        else:
            print("invalid choice")
    elif choice == ('3'):
        sys.exit()
    else:
        print("invalid choice\n")


def single_scan():
    print(" ")
    print("Single port scan.")
    print("____________________________________\n")
    print("Please enter IP you want to scan.\n")
    host = input(">>> ")
    print(" ")
    port = int(input("Please enter port "))
    print("____________________________________\n")
    print("Results for IP address: " + str(host))
    print("____________________________________\n")


    def portscanner(port): # checks to see if port is open or closed.
        if sock.connect_ex((host,port)):
            print("[*] Port %d is closed\n" % (port))
        else:
            print("[*] Port %d is open\n" % (port))

    portscanner(port)


def Scan_all():
    print(" ")
    print("Multiple Port scan.")
    print("____________________________________\n")
    print("Please enter IP you want to scan.\n")
    host = input(">>> ")
    print("____________________________________\n")
    print("Results for IP address: " + str(host))
    print("____________________________________\n")


    def portscanner(port): # checks to see if port is open or closed.
        if sock.connect_ex((host,port)):
            print(colored("[*] Port %d is closed\n" % (port), 'red'))
        else:
            print(colored("[*] Port %d is open\n" % (port), 'green'))

    for port in range(1,65535):
        portscanner(port)

while True:
    def start():
        menu()

    start()

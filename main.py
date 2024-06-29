# Simple port scanner.

import socket
import time
import os

def main():
    time.sleep(0.3)
    os.system("cls")
    ports = []
    print("## Simple port scanner ## - coolpancakes on github\n")
    ip_addr = input("Enter IP address to scan: ")
    print("Enter a range of ports by doing the following, EX:  1,2,55,33,66")
    port_range = input("Enter port or port range: ")
    ports.append(port_range.split(","))

    print("\n{}".format(ip_addr))
    for port_list in ports:
        for port in port_list:
            try:
                scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                scanner.settimeout(2)
                scanner_results = scanner.connect_ex((ip_addr, int(port)))
                if scanner_results == 0:
                    print("Port {} is open! ".format(port))
                else:
                    print("Port {} is closed. ".format(port))
            except ValueError:
                print("The port format is incorrect. ")
            except socket.gaierror:
                print("The IP format is incorrect. ")


if __name__ == "__main__":
    main()

# Title: NetBomb
# Description: Automated netork scanner with hacking features
# AUTHOR: DAZUM

import os, sys, time, threading, tkinter, socket


## COLOR
black="\033[0;30m"
red="\033[0;31m"
bred="\033[1;31m"
green="\033[0;32m"
bgreen="\033[1;32m"
yellow="\033[0;33m"
byellow="\033[1;33m"
blue="\033[0;34m"
bblue="\033[1;34m"
purple="\033[0;35m"
bpurple="\033[1;35m"
cyan="\033[0;36m"
bcyan="\033[1;36m"
white="\033[0;37m"
nc="\033[00m"
##

## LISTS
tryPorts = [21,22,80,194,443,8080,445,389,88,135,515,631,1080,3306,3389,9100]
openPorts = []
printer = []
activeHosts = []
menu = ""
##

def portScanner(): # The main scan function
    networkIp = input(f"\nPlease enter your range of {byellow}IP{nc} (for example, '192.168.0')\n\n{bblue}[NetBomb] {bcyan}>>{bred} ")

    for endIp in range(1,255):
        host = networkIp + "." + str(endIp) 

        for port in tryPorts:  
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.02)
            result = sock.connect_ex((host, port))
            
            if result == 0:
                print (f"{nc}{host}:{port}: Open")
                openPorts.append(host)
                openPorts.append(port)
                
                if host in activeHosts:
                    pass
                
                else:
                    activeHosts.append(host)
                
                match port:
                    case 515:
                        if host in printer:
                            pass
                        else:
                            printer.append(host)
                    case 631:    
                        if host in printer:
                            pass
                        else:
                            printer.append(host)
                    case 9100:    
                        if host in printer:
                            pass
                        else:
                            printer.append(host)
            sock.close()
    typeCounter(menu)
    
def typeCounter(menu):
    menu = f"\n\nThere are {len(activeHosts)} {bgreen}connected{nc} hosts\n\n"
    
    if len(printer) == 1:
        menu += "There is a printer\n\n"

    else:
        menu += f"There are {len(printer)} printers\n\n"
    
    if printer:
        menu += "[PR] Connect to printers\n"

    menuSelector(menu)

def menuSelector(menu):    

    print(menu)
    menuSelection = input(f"{bblue}[NetBomb] {bcyan}>>{bred} ")

    match menuSelection:
        case "PR":
            print(f"Connecting to {bgreen}printers{nc}....")
            printerScanner()
        
        case "pr":
            print(f"Connecting to {bgreen}printers{nc}....")
            printerScanner()
        
        case "exit":
            print(f"{bblue}[NetBomb]{nc} Exiting...")
            sys.exit(1)
        case _:
            print("select an option")
            menuSelector(menu)

def printerScanner():
    menu = ""
    for printers in printer:
        print(printers)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((printers, 9100))
        sock.sendall(b"@PJL INFO ID\n")
        data = sock.recv(1024).decode("utf-8")
        print("\n\nCONNECTION ACCEPTED\n\n",printer, f" {byellow}PRINTER TYPE: {red}", data, f"{nc}")
        menu += f" {byellow}PRINTER TYPE: {red}", data, f"{nc}"
    
    menuSelector(menu)




if __name__ == "__main__":
    portScanner()
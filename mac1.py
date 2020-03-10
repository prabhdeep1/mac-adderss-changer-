#!usr/bin/env python

import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change mac address")
    parser.add_option("-m", "--mac", dest="mac", help="enter new mac")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify a interface, use --help for more information")
    elif not options.mac:
        parser.error("[-] Please specify a new mac address, use --help for more information")
    return options


def change_mac(interface, mac):
    print("[+] changing mac for " + interface + " to " + mac)
    subprocess.call("ifconfig " + interface + " down", shell=True)
    subprocess.call("ifconfig " + interface + " hw ether " + mac, shell=True)
    subprocess.call("ifconfig " + interface + " up", shell=True)

def mac_current(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])

    mac_result_add = re.search(r"\w\w:\w\w\:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_result_add:
        return mac_result_add.group(0)
    else:
        print ("[-] could not read mac address")

options = get_arguments()

current_mac = mac_current(options.interface)
print("current mac = " + str(current_mac))
change_mac(options.interface, options.mac)


current_mac = mac_current(options.interface)
if current_mac == options.mac:
    print("[+] mac changed successfully")
else :
    print ("[-] mac did not change")



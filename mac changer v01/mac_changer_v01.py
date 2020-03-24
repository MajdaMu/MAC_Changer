#!/usr/local/bin/env python

# Version 01 of the mac_changer programs
# This program works with Python versions 2.7 and 3.7

# Subprocess is the module used to enable commands usage inside python code.
import subprocess

# The variables used to change the mac address.
interface = "eth0"
new_mac = "00:11:22:33:44:55"

subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)

print("[+] The MAC address of " + interface + " was changed successfully.")


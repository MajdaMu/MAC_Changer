#!/usr/local/bin/env python

# Version 02 of the mac_changer program
# This program works with Python versions 3.7

# Subprocess is the module used to enable commands usage inside python code.
import subprocess


# Using variables to make the change more flexible
interface = input("Enter the interface name: ")
new_mac = input("Enter the new mac address: ")

print("[+] Launching the program to change the MAC address of interface " + interface)

# The same commands used before, however, the values of the variables are entered by
# the user to make the program user friendly.
subprocess.call("ifconfig " + interface + " down", shell=True)
print("[+] Disabling the interface")

subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
print("[+] Changing the MAC address of the interface to the value provided")

subprocess.call("ifconfig " + interface + " up", shell=True)
print("[+] Enabling the interface")


# A print statement that indicates the success of the commands ran
print("[+] The change was successful.")


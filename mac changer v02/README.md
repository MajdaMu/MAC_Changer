# mac changer v02:
This program is a revised version of the *mac changer v01* program posted earlier. A few changes are made to the code to make it user friendly. Explinations of the changes are discussed below including the reasons for making such changes.

# How to use this program?
This portion includes the step by step process that allows the user to use the program.

### 01 - installation:
First you need to download, copy, or clone this repository. The following figure illustrates how you can download or clone the repository. <br/> 
![](https://github.com/MajdaMu/MAC_Changer/blob/master/mac%20changer%20v02/images/download.png)

### 02 - Find the downloaded file:
Afterward, navigate to the folder where you downloaded the *MAC_Changer* repository using the command line. Find the *mac changer v02* folder in the *MAC_Changer* project folder.

### 03 - Check your current MAC address:
After you find the location of the *mac_changer_v02.py*, check your current MAC address value by using the following command.<br/>
```

sudo ifconfig

```
The output will include multiple line that has your Inet number(IP), subnet mask, broadcast, ether, and much more. Your MAC address is the *ether* value. The following figure shows a sample output. <br/>

![](https://github.com/MajdaMu/MAC_Changer/blob/master/mac%20changer%20v02/images/current-mac.png)

### 04 - Run the program:
Now that we know the current MAC address value and where the file *mac_changer_v02.py* is stored, we can run the file. Keep in mind that because **sudo** is used, the system will ask you occasionally for the **root** password to make sure that you have the authority to modify the system running. Newer releases of Debian based Linux systems needs **sudo** to run programs like mac changer. To run the program type the following command:<br/>

```

sudo python3 mac_changer_v02.py

```

the program will prompt you with the following questions: (The values are examples only, change them please) <br/>

```

Enter the interface name: *eth0*
Enter the new mac address: *00:xx:xx:xx:xx:xx*

```

Enter the values of the interface and the mac address. **This part of the program was added to make the user more comfortable by allowing them to run all the commands using a shell instead of opening a text editor. Also, messages that indicate the processes ran will appear, and if errors appear they will follow the process that did not run.** When the code has finished running the following output will appear: <br/>

![](https://github.com/MajdaMu/MAC_Changer/blob/master/mac%20changer%20v02/images/mac-changer-output.png)

# Errors:
This section includes some possible errors that the user might encounter while running the *mac_changer_v02.py*.

### error01 - Code problem:
The following error message will only appear if the code was changed. Specifically, if the "**subprocess.call**" function does not have the **, shell=True** at the end of the function. 

```

[+] Disabling the interface
Usage:
  ifconfig [-a] [-v] [-s] <interface> [[<AF>] <address>]
  [add <address>[/<prefixlen>]]
  [del <address>[/<prefixlen>]]
  [[-]broadcast [<address>]]  [[-]pointopoint [<address>]]
  [netmask <address>]  [dstaddr <address>]  [tunnel <address>]
  [outfill <NN>] [keepalive <NN>]
  [hw <HW> <address>]  [mtu <NN>]
  [[-]trailers]  [[-]arp]  [[-]allmulti]
  [multicast]  [[-]promisc]
  [mem_start <NN>]  [io_addr <NN>]  [irq <NN>]  [media <type>]
  [txqueuelen <NN>]
  [[-]dynamic]
  [up|down] ...

  <HW>=Hardware Type.
  List of possible hardware types:
    loop (Local Loopback) slip (Serial Line IP) cslip (VJ Serial Line IP) 
    slip6 (6-bit Serial Line IP) cslip6 (VJ 6-bit Serial Line IP) adaptive (Adaptive Serial Line IP) 
    ash (Ash) ether (Ethernet) ax25 (AMPR AX.25) 
    netrom (AMPR NET/ROM) rose (AMPR ROSE) tunnel (IPIP Tunnel) 
    ppp (Point-to-Point Protocol) hdlc ((Cisco)-HDLC) lapb (LAPB) 
    arcnet (ARCnet) dlci (Frame Relay DLCI) frad (Frame Relay Access Device) 
    sit (IPv6-in-IPv4) fddi (Fiber Distributed Data Interface) hippi (HIPPI) 
    irda (IrLAP) ec (Econet) x25 (generic X.25) 
    eui64 (Generic EUI-64) 
  <AF>=Address family. Default: inet
  List of possible address families:
    unix (UNIX Domain) inet (DARPA Internet) inet6 (IPv6) 
    ax25 (AMPR AX.25) netrom (AMPR NET/ROM) rose (AMPR ROSE) 
    ipx (Novell IPX) ddp (Appletalk DDP) ec (Econet) 
    ash (Ash) x25 (CCITT X.25) 

```
To correct this error you will have to open the *mac_changer_v02.py* file and make sure that the function "**subprocess.call**" ends with "**, shell=True**". Do not forget the comma to seperate the command from the state of the command which is "**True**" in this specific case. By assigning "*True*" to the "*shell*" argument, you are telling python that it has the authority to run the commands in the shell. <br/>

### error 02 - Authoritative problem:
This error will appear when you forget to enter "**sudo**" before running the "*ifconfig*" command and the "*sudo python xxx*". <br/>
```

Traceback (most recent call last):
  File "mac_changer_v02.py", line 8, in <module>
    from pip._vendor.distlib.compat import raw_input
ImportError: No module named pip._vendor.distlib.compat

```
This error will also appear to tell you that you need to specify the version of python you want to run the program. To resolve this problem enter the following command to run the program:<br/>

```

sudo python3 mac_changer_v02.py

```
If you prefer to change the code, just change the "**input**" statement to the following: *(keep in mind, if you decide to do this option instead of the previous one it means that you are running python 2.7, which means that you should take out the "**3**" out of your command to run the code)* <br/>
```

interface = raw_input()
new_mac = raw_input()

```
# Coming Up:
This program improves the user experience by letting the user run the program without needing to change the code. As well as, giving the user notifications (**messages**) that indicate the progress of the program while running and after it finishes. Even though this program is much improved from the previous version, it could still be improved further. A version 03 might need to be created in the future; an explination of the version will be included if a third version is published. Enjoy the imporovments made! 


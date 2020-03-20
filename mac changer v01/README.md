# mac_changer_v01.py

This program includes a basic MAC address (*Physical address*) changer. This folder includes the first version of 
the mac_changer program which makes this version fairly basic. As a result this version requires the user to change 
the values of the variables *"interface"* and *"new_mac"* inside the *.py* file using a text editor or an IDE. 

# How to use the program?

1- Please download, clone, or copy the program into the Linux distribution you are using. <br/>
*To Download or Clone the MAC_Changer repository:* <br/>  
![](https://github.com/MajdaMu/MAC_Changer/blob/master/mac%20changer%20v01/images/download.png)
 
2- Use the command line to navigate to the place where *mac_changer_v01.py* is installed. 
 
3- After reaching the folder containing *mac_changer_v01.py*, check your current MAC address value by typing: 
```

sudo ifconfig

```
The MAC address value is next to the *ether* word which is highlighted with a red border in the image below.
 
![](https://github.com/MajdaMu/MAC_Changer/blob/master/mac%20changer%20v01/images/check-current-mac.png)<br/>

4- Next open the *mac_changer_v01.py* using your favorite text editor or IDE. Or you can use nano which is installed 
already with most
Linux distros. To open nano enter the following command: <br/>

```

nano mac_changer_v01.py

```

5- Change the values of the *"interface"* and *"new_mac"* variables to the values you want. <br/>
```

# The variables used to change the mac address.
interface = "eth0"
new_mac = "00:11:11:11:11:11"

```

6- Now that you have changed the values in nano you can press the following keys to save and exit from nano.

```

ctrl + x

y

enter

```

7- Now you can run the program using the following command:
```

sudo python mac_changer_v01.py

```

If the command runs successfully, the following output should appear:
```

[+] The MAC address of [interface name] was changed successfully.

```

# Errors:
Most errors appear because almost all the new updates of Linux distros require the user to enter *sudo* before any command that
will change the hardware information of the device or virtual machine. So if you faced any errors that says:
```

/bin/sh: 1: ifconfig: not found
/bin/sh: 1: ifconfig: not found
/bin/sh: 1: ifconfig: not found

```
Or 
```

bash: ifconfig: command not found

```

Try using *sudo* before running the *ifconfig* or the *mac_changer_v01.py* program. Also, keep 
in mind that *sudo* will ask you occasionally for the root password to make sure that you have the authority to 
modify the system running. 


# Coming up:

This program is a good start and it completes the task we wanted it to accomplish; it changes the MAC address 
and can be used for all Debian based Linux distributors. However, it can be improved so 
another version of the program will be uploaded soon.


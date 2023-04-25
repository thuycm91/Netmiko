#import netmiko
from netmiko import ConnectHandler

#dictionary, object
Router = {
    "device_type": "cisco_ios",
    "ip": "10.18.8.150",
    "username": "vnpro",
    "password": "vnpro#123",
    "secret": "vnpro#321" #password enable
}
#user, privileges, config
connect = ConnectHandler(**Router)

connect.enable() #unpack

#send_config_set function
#print(connect.send_config_set("hostname R1-Netmiko-Python"))
print(connect.send_config_set(["int lo1", "no shut", "ip add 192.168.2.2 255.255.255.224"]))

#use for loop

#for i in range (1, 4):
#    print(connect.send_config_set(["int lo" + str(i), "no shut", "ip add 10.10."+ str(i) +".2 255.255.255.224"]))

#send_command 
print(connect.send_command("show ip int br")) #lenh day du hoac viet tat

#string, interger, float(1.2, 8.4)
#concatenate, parse(convert)

#"""
#"lo1": "10.10.1.1"
#"lo2": "10.10.2.1"
#"lo3": "10.10.3.1"
#"""

interfaces = {
    "lo1": "10.10.1.1",
    "lo2": "10.10.2.1",
    "lo3": "10.10.3.1"
}

for i in interfaces:
    print(connect.send_config_set(["int "+ i,"ip addr " + interfaces[i]+ " 255.255.255.0", "no shut" ]))

#send_command 
print(connect.send_command("show ip int br")) #lenh day du hoac viet tat

#disconnect
connect.disconnect()




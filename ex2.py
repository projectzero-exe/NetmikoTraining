from netmiko import ConnectHandler
from getpass import getpass


myDevice = {"device_type": "cisco_nxos",
           "host": "nxos1.lasthop.io",
           "username": "pyclass",
           "password": getpass()}

connect = ConnectHandler(**myDevice)
print(connect.find_prompt())
print(connect.send_command("show ip int br"))

connect.disconnect()
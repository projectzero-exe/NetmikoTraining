from netmiko import ConnectHandler
from getpass import getpass

connect = ConnectHandler(device_type="nxos", host="nxos1.lasthop.io", username=pyclass, password=getpass())

print(connect.find_prompt())

connect.disconnect()
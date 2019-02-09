# By Jacob Ouellette
import netifaces as ni
import netifaces
print('{0:15}{1:20}{2:10}'.format("Interfaces", "IPv4", "Netmask"))
print('----------------------------------------------------')
for interface in ni.interfaces():
	ni.ifaddresses(interface)
	ip = ni.ifaddresses(interface)[ni.AF_INET][0]['addr']
	mask = ni.ifaddresses(interface)[ni.AF_INET][0]['netmask']
	print('{0:15}{1:20}{2:10}'.format(interface, ip, mask))

gw_if = netifaces.gateways()['default'][netifaces.AF_INET][1]		# Get gateway interface
gw_addr = netifaces.gateways()['default'][netifaces.AF_INET][0]		# Get gateway address
print("\nDefault gateway is",gw_addr,"via",gw_if)


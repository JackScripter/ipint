# ipint
Show ip addresses

Installation
-
You need to have python3-pip installed or python3-netifaces.
```
git clone https://github.com/JackScripter/ipint.git
sudo ./ipint/install.sh
```

Usage
-
```
[root@localhost ~]# ipint
Interfaces     IPv4                Netmask
----------------------------------------------------
lo             127.0.0.1           255.0.0.0
enp0s29        10.50.0.1           255.255.255.0
enp8s4         192.168.55.79       255.255.255.0
vmnet1         192.168.254.1       255.255.255.0
vmnet2         192.168.11.254      255.255.255.0
vmnet3         172.16.0.1          255.255.255.0
vmnet4         172.16.1.1          255.255.255.0
vmnet5         10.0.5.1            255.255.255.248
vmnet6         10.0.7.9            255.255.255.248
vmnet7         172.16.15.1         255.255.255.0
vmnet8         172.16.226.1        255.255.255.0

Default gateway is 192.168.55.1 via enp8s4
```

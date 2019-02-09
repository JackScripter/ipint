#!/bin/bash
if [[ $EUID -ne 0 ]]; then
        echo "This script must be run as root"
        exit 1
fi # Check if the script is run as root
if ! pip3 list --format=legacy | grep -s netifaces &>> /dev/null; then pip3 install netifaces; fi
python3 <<< "import py_compile; py_compile.compile('ipint.py')"
mv -v __pycache__/*.pyc /usr/bin/ipint
rm -rv __pycache__
chmod -v +x /usr/bin/ipint && echo "Installation success" || echo "Error occured"

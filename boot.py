# boot.py

import machine
from network import WLAN
from include.secrets import _ssid, _pass

wlan = WLAN()  # get current object, without changing the mode


if machine.reset_cause() != machine.SOFT_RESET:
    wlan.init(mode=WLAN.STA)
    # configuration below MUST match your home router settings!!
    # wlan.ifconfig(config=('192.168.178.107', '255.255.255.0', '192.168.178.1', '8.8.8.8'))

if not wlan.isconnected():
    # change the line below to match your network ssid, security and password
    wlan.connect(_ssid, auth=(WLAN.WPA2, _pass), timeout=5000)
    while not wlan.isconnected():
        machine.idle()  # save power while waiting

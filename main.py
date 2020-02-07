'''
Beautiful it ain't. But I made it in an afternoon so pbbbbththtttthh.

Hit the button, Max.
'''


from machine import Pin
from uosc.client import Client
import time
import network
print("main.py loaded")

button1 = Pin(34, Pin.IN)
button2 = Pin(35, Pin.IN)

console = Client('192.168.1.162', 53000)
#ESP32-GATEWAY board rev C and above require the clock_mode parameter in network setup
nic = network.LAN(mdc = Pin(23), mdio = Pin(18), phy_type = network.PHY_LAN8720, phy_addr = 0, clock_mode = network.ETH_CLOCK_GPIO17_OUT)

def networkConnect():
    if not nic.isconnected():
        nic.active(True)
        nic.ifconfig(('192.168.1.254', '255.255.255.0','192.168.1.1', '192.168.1.1'))
    print(nic.ifconfig())

#DRY, eh? Hah!

def player1():
    console.send('/cue/1/start')
    print("player1 sent")
    time.sleep(5)

def player2():
    console.send('/cue/2/start')
    print("player2 sent")
    time.sleep(5)

while True:
    if not nic.isconnected():
        networkConnect()
    if nic.isconnected():
        if button1.value() == 1:
            player1()
        if button2.value() == 1:
            player2()

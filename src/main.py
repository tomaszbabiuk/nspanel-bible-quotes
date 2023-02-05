import network
import json
from machine import UART
from nextion import *
from quotes import createBibleActions

uart = UART(2, 115200)
uart.init(115200, bits=8, parity=None, stop=1, tx=16, rx=17)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

writer = NextionWriter(uart)

actionsBag = []
createBibleActions(actionsBag, writer)
reader = NextionReader(uart, actionsBag)

while True:
    reader.readAndParse()
    time.sleep_ms(50)

# quotes = []
# with open("quotes.json", "r") as f:
#     quotes = json.load(f)["pl"]

# print(quotes)
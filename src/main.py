import asyncio
from kasa import SmartBulb
import tkinter as tk

# IP Address of the Smart Bulb
IP_ADDRESS = "192.168.1.141"

# Function to get the current status of the bulb
async def get_bulb_status():
    bulb = SmartBulb(IP_ADDRESS)
    await bulb.update()
    return bulb.is_on

# Function to turn the bulb ON
async def turn_on_bulb():
    bulb = SmartBulb(IP_ADDRESS)
    await bulb.turn_on()

# Function to turn the bulb OFF
async def turn_off_bulb():
    bulb = SmartBulb(IP_ADDRESS)
    await bulb.turn_off()

# Function to handle button clicks
def handle_button_click(action):
    asyncio.run(turn_on_bulb() if action == "on" else turn_off_bulb())

# Set up the Tkinter GUI
root = tk.Tk()
root.title("Smart Bulb Controller")

# Creating ON and OFF buttons
tk.Button(root, text="Turn ON", command=lambda: handle_button_click("on")).pack(pady=10)
tk.Button(root, text="Turn OFF", command=lambda: handle_button_click("off")).pack(pady=10)

# Start the GUI loop
root.mainloop()

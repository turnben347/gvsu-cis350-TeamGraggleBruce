import asyncio
from kasa import SmartBulb
import tkinter as tk

# IP address of the bulb
IP_ADDRESS = "192.168.1.141"

# Set to none to prevent lots of functions calls slowing the slider
brightness_update_task = None


# Function to get current status of bulb
async def get_bulb_status():
    bulb = SmartBulb(IP_ADDRESS)
    await bulb.update()
    return bulb.is_on


# Function to turn the bulb on with brightness
async def turn_on_bulb_with_brightness(brightness):
    bulb = SmartBulb(IP_ADDRESS)
    await bulb.update()
    await bulb.set_brightness(brightness)
    await bulb.turn_on()


# Function to turn the bulb off
async def turn_off_bulb():
    bulb = SmartBulb(IP_ADDRESS)
    await bulb.turn_off()


# Function to toggle the bulb state, setting brightness when turning on
async def toggle_bulb():
    bulb = SmartBulb(IP_ADDRESS)
    await bulb.update()
    if bulb.is_on:
        await bulb.turn_off()
    else:
        # Set brightness when turning on
        brightness = max(1, brightness_slider.get())
        await turn_on_bulb_with_brightness(brightness)


# Function to toggle button click
def handle_toggle():
    asyncio.run(toggle_bulb())
    update_toggle_button_text()


# Function to update toggle button text
def update_toggle_button_text():
    is_on = asyncio.run(get_bulb_status())
    toggle_button.config(text="Turn off" if is_on else "Turn on")


# Function to set brightness of the bulb with slider
async def set_brightness(level):
    bulb = SmartBulb(IP_ADDRESS)
    await bulb.update()
    if bulb.is_on:
        await bulb.set_brightness(level)


# Function to handle brightness slider change with delay for responsiveness
def handle_brightness_change(value):
    global brightness_update_task
    brightness = max(1, int(value))
    # Cancel the previous task if it exists
    if brightness_update_task:
        root.after_cancel(brightness_update_task)
    # Set a delay before calling set_brightness
    brightness_update_task = root.after(200, lambda: asyncio.run(set_brightness(brightness)))


# Set up the GUI
root = tk.Tk()
root.title("Smart Light")
root.geometry("400x400")

# Create button for on off
toggle_button = tk.Button(root, command=handle_toggle)
toggle_button.pack(pady=10)

# Create brightness slider
brightness_slider = tk.Scale(root, from_=1, to=100, orient="horizontal", label="Brightness",
                             command=handle_brightness_change)
brightness_slider.pack(pady=10)

# Initialize button text based on bulb status
update_toggle_button_text()

# Start the GUI
root.mainloop()

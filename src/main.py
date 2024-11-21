import asyncio
from kasa import SmartBulb
import tkinter
from tkinter import colorchooser
from colorsys import rgb_to_hsv

# ip of the bulb
BULB_IP = "192.168.1.141"

# global vars for stuff we need later
window = tkinter.Tk()
brightness_slider = None
on_off_button = None
last_brightness_update = None


# turns bulb on and sets how bright it is
async def turn_on_with_brightness(bright_level):
    my_bulb = SmartBulb(BULB_IP)
    await my_bulb.update()
    await my_bulb.set_brightness(bright_level)
    await my_bulb.turn_on()


# turns off the bulb
async def turn_off():
    my_bulb = SmartBulb(BULB_IP)
    await my_bulb.turn_off()


# checks if bulb is on or off
async def is_bulb_on():
    my_bulb = SmartBulb(BULB_IP)
    await my_bulb.update()
    return my_bulb.is_on


# handles the brightness slider moving
def brightness_changed(value):
    global last_brightness_update

    # cancel old update if it exists
    if last_brightness_update:
        window.after_cancel(last_brightness_update)

    # make sure brightness isn't 0
    brightness = max(1, int(float(value)))

    # wait a bit before updating to make it smoother
    last_brightness_update = window.after(200, lambda: asyncio.run(update_brightness(brightness)))


# actually updates the bulb brightness
async def update_brightness(level):
    my_bulb = SmartBulb(BULB_IP)
    await my_bulb.update()
    if my_bulb.is_on:
        await my_bulb.set_brightness(level)


# changes the color of the bulb
async def change_bulb_color(color):
    my_bulb = SmartBulb(BULB_IP)
    await my_bulb.update()

    if my_bulb.is_on:
        # convert RGB to what the bulb needs
        r = color[0] / 255.0
        g = color[1] / 255.0
        b = color[2] / 255.0

        hsv = rgb_to_hsv(r, g, b)

        hue = int(hsv[0] * 360)
        sat = int(hsv[1] * 100)
        val = brightness_slider.get()

        await my_bulb.set_hsv(hue, sat, val)


# opens color picker window
def pick_color():
    color = colorchooser.askcolor(title="Change color")[0]
    if color:
        rgb = (int(color[0]), int(color[1]), int(color[2]))
        asyncio.run(change_bulb_color(rgb))


# turns bulb on/off when button clicked
def button_clicked():
    asyncio.run(toggle_bulb())
    update_button()


# actually toggles the bulb
async def toggle_bulb():
    my_bulb = SmartBulb(BULB_IP)
    await my_bulb.update()

    if my_bulb.is_on:
        await my_bulb.turn_off()
    else:
        bright = max(1, brightness_slider.get())
        await turn_on_with_brightness(bright)


# updates the button text
def update_button():
    is_on = asyncio.run(is_bulb_on())
    on_off_button.config(text="Turn OFF" if is_on else "Turn ON")


# make the window
window.title("Light Control")
window.geometry("250x250")

# make the on/off button
on_off_button = tkinter.Button(window, command=button_clicked)
on_off_button.pack(pady=20)

# make the brightness slider
brightness_slider = tkinter.Scale(window, from_=1, to=100,
                                  orient="horizontal",
                                  label="Brightness",
                                  command=brightness_changed)
brightness_slider.pack(pady=20)

# make the color button
color_button = tkinter.Button(window, text="Change Color", command=pick_color)
color_button.pack(pady=20)

# set initial button text
update_button()

# start the program
window.mainloop()

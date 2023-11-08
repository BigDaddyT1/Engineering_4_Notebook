import adafruit_mpu6050 
import busio
import board
import time 
import adafruit_displayio_ssd1306
import digitalio
import terminalio
import displayio
from adafruit_display_text import label


displayio.release_displays() # this needs to be first in the code
sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP6)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64) # pin address and setup for oled display

# create the display group
splash = displayio.Group()

# add title block to display group
title = "ANGULAR VELOCITY"
# the order of this command is (font, text, text color, and location)
text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5)
splash.append(text_area)    
# send display group to screen
display.show(splash)


led1 = digitalio.DigitalInOut(board.GP4)
led1.direction = digitalio.Direction.OUTPUT


mpu = adafruit_mpu6050.MPU6050(i2c)
mpu.gyro
# tells the angles of the code and tells the code to run through on repeat.



while True:
    acc = mpu.acceleration # new var
    print(f"X: {acc[0]} m/s^2 Y: {acc[1]} m/s^2 Z: {acc[2]} m/s^2") # print x, y, and z values
    gyro = mpu.gyro # new var for gyro
    text_area.text = f"X: {gyro[0]: .3f}rad/s\nY: {gyro[1]: .3f}rad/s\nZ: {gyro[2]: .3f}rad/s"  # print the values on the oled display, .3f means 3 decimal point
    # \n breaks the line and goes to next row for the following text
    print(f" x angular acceleration {mpu.acceleration[0]}")
    print(f" y angular acceleration {mpu.acceleration[1]}")
    print(f" z angular acceleration {mpu.acceleration[2]}")
    print("")
    print("")
    time.sleep(1.5)

    if mpu.acceleration[2]<4:
        led1.value = True

    else:
        led1.value=False    
    
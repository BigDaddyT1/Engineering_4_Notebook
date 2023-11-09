
import time
import terminalio
import displayio
import busio    
import board
from adafruit_display_text import label
import adafruit_displayio_ssd1306
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.circle import Circle
from adafruit_display_shapes.line import Line

displayio.release_displays() # this needs to be first in the code
sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP6)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64) # pin address and setup for oled display

# create the display group
splash = displayio.Group()

		### couculates the area of object 
def triangle_area( x1y1, x2y2, x3y3):
    #try:
		### tels code to request info 
        [x1,y1]= x1y1.split (',')
        [x2,y2]= x2y2.split (',')
        [x3,y3]= x3y3.split (',')

		#pull strings into floats 
        splash.append(Circle(64, 32, 3, outline=0xFFFFFF))
        splash.append(Line(0, 32, 128, 32, 0xFFFFFF))
        splash.append(Line(64, 0, 64, 64, 0xFFFFFF)) #add base and coordinate axes
        triangle = Triangle(int(x1)+64,32-int(y1), int(x2)+64, 32-int(y2), int(x3)+64,32-int(y3), outline=0xFFFF00)
        splash.append(triangle)
        display.show(splash)# communicates to show display 
        # add title block to display group
        title = "ANGULAR VELOCITY"
        # the order of this command is (font, text, text color, and location)
        text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5)
        splash.append(text_area)    
        # send display group to screen
        area=abs((int(x1)*(int(y2)-int(y3))+int(x2)*(int(y3)-int(y1))+int(x3)*(int(y1)-int(y2)))/2)

        return area 
while True: 
    ### makes me request input from the user 
        Val1 = input("Enter the first cordinate in format x,y:    ")
        Val2 = input("Enter the second cordinate in format x,y:   ")
        Val3 = input("Enter the third cordinate in format x,y:    ")
        area = triangle_area(Val1, Val2, Val3)
        if area == 0:
            continue
        
        else:
            print(f"({Val1}) this is cordinate 1 ({Val2}) this is cordinate 2 ({Val3}) this is cordinate 3 ({area}) area")
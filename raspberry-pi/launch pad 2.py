import time 
import digitalio
import board
led1 = digitalio.DigitalInOut(board.GP15)
led1.direction = digitalio.Direction.OUTPUT
led2 = digitalio.DigitalInOut(board.GP16)
led2.direction = digitalio.Direction.OUTPUT


# Using reversed()
for x in reversed(range(1,11)):
#for x in range(11):\
#Runs red led 10-1 then at zero will run wile true statment.
    print(x)
    led1.value = True
    time.sleep(.5)
    led1.value = False
    time.sleep(.5)
# when loop finishes light turns green
while True:
    led2.value = True 
    print(0)
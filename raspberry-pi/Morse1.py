import board
import digitalio
import time
led = digitalio.DigitalInOut(board.GP15)
led.direction = digitalio.Direction.OUTPUT

# Dictionary representing the morse code chart
MORSE_CODE = { 'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-'}
modifier = 0.25
dot_time = 1*modifier
dash_time = 3*modifier
between_taps = 1*modifier
between_letters = 3*modifier
between_words = 7*modifier
translated_message = ''# tells the code to put a space inbetween the code.

while True:
    message = input("MORSE_CODE message: ") # tells computer to ask for message 
    print(message)
    if message == '-q':# if the user types in a lowercase -q quit
            break
    message= message.upper()# turns lowercase into upercase 
    print(message)

    for letter in message:
        translated_message = translated_message + ' ' + MORSE_CODE[letter] # tells code to do translated message plus a space for the morse code to stay in one line. 

    print(translated_message) # this prints the code

    for character in translated_message: #loop thru morse message
        print(character)
        if character == ".":
            led.value = True
            time.sleep(dot_time)
            led.value = False
        if character == "/":
            led.value = True
            time.sleep(between_taps)
            led.value = False
        if character == " ":
            led.value = True
            time.sleep(between_letters)
            led.value = False
        if character == "-":
            led.value = True
            time.sleep(dash_time)
            led.value = False

        time.sleep(dot_time)

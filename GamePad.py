#!/usr/bin/python
from evdev import InputDevice
game_pad = InputDevice('/dev/input/event12')
# event12 is this device. this number may change if the
# program is used on a different computer. run 
# "python -m evdev.evtest" to find which event the 
# device is connected to and modify code as needed.

debug = False	# force an output when a button is pressed if debug = True

# constant types, codes, and values
DIG_TYPE = 1    # digital type press
ALG_TYPE = 3    # analog type button
LSH_CODE = 0    # D-Pad horizontal code
LSV_CODE = 1    # D-Pad vertical code
LT_CODE = 2     # left trigger code
RSH_CODE = 3    # right stick horizontal code
RSV_CODE = 4    # right stick vertical code
RT_CODE = 5     # right trigger code
DPH_CODE = 16   # left stick horizontal code
DPV_CODE = 17   # left stick vertical code
BTN_A_CODE = 304    # button A code
BTN_B_CODE = 305    # button B code
BTN_X_CODE = 307    # button X code
BTN_Y_CODE = 308    # button Y code
L_BMP_CODE = 310    # left bumper code
R_BMP_CODE = 311    # right bumper code
SEL_CODE = 314      # select button code
START_CODE = 315    # start button code
LOGI_CODE = 316     # logitech button code
L_STK_CODE = 317    # left stick code
R_STK_CODE = 318    # right stick code
KEY_UP_VAL = 0      # button up value
KEY_DOWN_VAL = 1    # button down value
KEY_HOLD_VAL = 2    # button hold value

print(game_pad)     # print the name of the device in use
print("\n")  

for event in game_pad.read_loop():  # run while the controller is in use
    if debug is True:      
	print(event)
    elif event.type == DIG_TYPE:    # if the button pressed is digital...
        if event.value == KEY_DOWN_VAL:     # register the down strokes only
            if event.code == BTN_A_CODE:
                print "A"
            elif event.code == BTN_B_CODE:
                print "B"
            elif event.code == BTN_X_CODE:
                print "X"
            elif event.code == BTN_Y_CODE:
                print "Y"
            elif event.code == L_BMP_CODE:
                print "Left Bumper"
            elif event.code == R_BMP_CODE:
                print "Right Bumper"
            elif event.code == L_STK_CODE:
                print "Left Stick"
            elif event.code == R_STK_CODE:
                print "Right Stick"
            elif event.code == START_CODE:
                print "Start"
            elif event.code == SEL_CODE:
                print "Select"
            elif event.code == LOGI_CODE:
                print "Logitech"

    elif event.type == ALG_TYPE:    # if the button pressed is analog...
        if event.code == LSH_CODE:
            print(event.value)
        elif event.code == LSV_CODE:
            print(event.value)
        elif event.code == RSH_CODE:
            print(event.value)
        elif event.code == RSV_CODE:
            print(event.value)
        elif event.code == DPV_CODE:
            print(event.value)
        elif event.code == DPH_CODE:
            print(event.value)
        elif event.code == LT_CODE:
            print(event.value)
        elif event.code == RT_CODE:
            print(event.value)

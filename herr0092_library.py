# Fernando Herrera - 040960796
#   Library

import time
import random
from gfxhat import lcd, backlight
import math

# Function to print some label
def printTitle( message ):
    print('=====================')
    print(' ' + message )
    print('=====================')


# Function to calculate area
# @radius: int - radius of the circle
def calculateArea( radius ):
    area = math.pi * ( radius * radius)
    return area

# Function to calculate MPG
# m: float = minimun
# g: float = galons
def calculateMPG(m, g):
    mpg =  round(m / g, 2)
    return mpg

# Function to calculate MPG
# f: float = fahrenheit temperature
def calculateCelsius( f ):
    c = round( ( f - 32 ) * (5/9), 2)
    return c

# Calculate distance between two points
# x1,x2, y1, y2 MOST be integer values
def calculateDistanceBetweenPoints(x1,y1,x2,y2):
    xDistance = x1 - x2
    yDistance = y1 - y2
    a2 = xDistance ** 2
    b2 = yDistance ** 2

    return math.sqrt( a2 + b2 )





# To clear the screen
import subprocess as sp

def clearConsole():
    sp.call('clear',shell=True)

def showMenu():
    clearConsole()

    print('''
-=-=-=-=- Welcome =-=-=-=-
-     Choose wisely!     -
=                        =
-  1- Horizontal line    -
=  2- Vertical line      =
-  3- Basic Staircase    -
=  4- Custom Staricase   =
-  5- Random pixel       -
=                        =
-  0- Clear and Exit     -
=                        = 
-=-=-=-=-=-=-=-=-=-=-=-=-=
''')


def clearScreen():
    lcd.clear()
    lcd.show()
    backlight.set_all(200, 200, 200)
    backlight.show()

def rainbowFinish():
    for i in range(0,100): 
        setBgColor(255, 17, 0)
        setBgColor(255, 248, 1)
                    
def clearBacklight():
    setBgColor(0,0,0)

# Change the bgcolor
def setBgColor(r,g,b):
    backlight.set_all(r, g, b)
    backlight.setup()
    backlight.show()

def setRedBG():
    setBgColor(205, 36, 0)

def setGreenBG():
    setBgColor(27, 203, 26)


# Creates a vertical line at given x coordinate
def verticalLine( x ):
    print('Drawing....')
    setRedBG()
    for i in range(0,63):
        lcd.set_pixel(x, i, 1)
        lcd.show()
        time.sleep(0.02)
    print('Finished')
    setGreenBG()
    

#Creates a horizontal line at given y coordinate
def horizontalLine( y ):
    print('Drawing....')
    setRedBG()
    for i in range(0, 127):
        lcd.set_pixel(i, y, 1)
        lcd.show()
        time.sleep(0.02)
    print('Finished')
    setGreenBG()

# Default staircase
def defaultStaircase():
    staircase(30, 63, 5, 5)

# Creates a staircase
def staircase(x, y, w, h):
    # x = 30
    # y = 63
    print('Drawing...')
    setRedBG()
    while x < 127 and y >= 0:

        for i in range(0, w):
            x = x + 1
            if ( x > 127 ): 
                break

            lcd.set_pixel(x, y, 1)
            lcd.show()
        
        for i in range(0,h):
            y = y - 1
            if ( y < 0 ): 
                break
            lcd.set_pixel(x, y, 1)
            lcd.show()
    
    
    # lcd.show()
    print('Finished')
    setGreenBG()


# Displays a random pixel for X seconds
def randomPixel(t):

    now  = int(round(time.time() * 1000))
    exit = now + (t * 1000)

    while now <= exit:
        x = random.randint(0, 127)
        y = random.randint(0, 63)
        setPixel( x,y, 1 )
        
        now = int(round(time.time() * 1000))

        # setBgColor(40, 56, 142)
        setRedBG()
        setGreenBG()
        setRedBG()
        setBgColor(200,200,200)
    

def setPixel( x, y, on ):
    lcd.set_pixel(x, y, on)
    lcd.show()
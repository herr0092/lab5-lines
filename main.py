import herr0092_library as f
import time

def main():
    f.showMenu()

    opt = input('option (1-6): ' )

    if ( opt == '1' ):
        f.clearConsole()
        f.clearScreen()
        y = int(input( 'Enter Y coordinate (0-63): ' ))
        f.horizontalLine( y )

    elif ( opt == '2'):
        f.clearConsole()
        f.clearScreen()
        x = int(input( 'Enter X coordinate (0-127): ' ))
        f.verticalLine( x )

    elif ( opt == '3' ):
        f.clearConsole()
        f.clearScreen()
        f.defaultStaircase()

    elif ( opt == '4' ):
        f.clearConsole()
        f.clearScreen()
        x = int(input( 'Enter X coordinate (0-127): ' ))
        y = int(input( 'Enter Y coordinate (0-63): ' ))
        w = int(input( 'Enter width: ' ))
        h = int(input( 'Enter height: ' ))

        f.staircase(x, y, w, h)

    elif ( opt == '5'):
        f.clearConsole()
        f.clearScreen()
        print('Displaying a random pixel')
        timeout = int(input( 'For how many seconds: ' ))
        f.randomPixel( timeout )


    return opt

# Main and loop

opt = '1'
f.clearScreen()
f.clearConsole()
f.clearScreen()

while opt != '0':
    opt = main()
    
f.clearConsole()
f.clearScreen()
f.clearBacklight()
print('Have a nice day')
print('Bye bye!')
    
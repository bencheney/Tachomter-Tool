# Tachometer Tool Version 1.03 by Ben Cheney.
# The next implementation may be based on pysical inputs without keyed input.

# This is a complete re-write based on improved arguments 01.05.2019.
# Complacent with operation 01.06.2019.

# Output to tachometer is accurate below 2000 RPM, this may be a limitation of the
# transistor being used or current in the circuit - further research required to pinpoint.
# 01.07.2019

# 01.16.2019 - this alternate version has the RPI specific commands commented out to run
# on devices other than the RPi.

import time
#import RPi.GPIO as io # Comment out to run outside of RPi.

#io.setwarnings(False) # Comment out to run outside of RPi.

#io.setmode(io.BCM) # Comment out to run outside of RPi.
#io.setup(4,io.OUT) # Comment out to run outside of RPi.

c = 0
r = 0

print('\nTachometer Tool Version 1.03.\nThis version is input based.\n')

def cinput(c):
    c = int(input('Enter 4, 6, or 8 for the number of cylinders the tachometer is intended for: '))
    if (c != 4 and c != 6 and c != 8):
        print('\n',c, 'cylinders unsupported, please try again.\n')
        cinput(c)

    else:
        rinput(c, r)


def rinput(c, r):
    r = int(input('Enter RPM (revolutions per minute) between 500 and 6000: '))
    if (r < 500 or r > 6000):
        print('\n',r, 'RPM unsupported, please try again.\n')
        rinput(c, r)

    else:
        rate(c, r)


def rate(c, r):
    x = 0
    t = (1 / ((r * (c / 2)) / 60)) / 2
    # The actual formula is t = 1 / ((r * (c / 2)) / 60), the division by 2 is to compensate
    # for the period of time doubling in the while loop for the ON and OFF condition.

    print('\n',c, 'cylinders selected at',r,'RPM.')
    # print('\n',t*2, 'seconds is the pulse frequency.') # Only for reference.
    # Observe t*2 to compensate for formula adjustment.
    
    while x < 500 : # Improve duration period so it isn't proportionate to the rate.
      #io.output(4,0) # Comment out to run outside of RPi.
      #time.sleep(t) # Comment out to run outside of RPi.
      #io.output(4,1) # Comment out to run outside of RPi.
      #time.sleep(t) # Comment out to run outside of RPi.
      x = x + 1

    y = input('\nType Y to run the program again or press enter to exit: ')
    if y == 'Y' or y == 'y':
        cinput(c)

    else:
        print('\nThanks for using the program!')

cinput(c)

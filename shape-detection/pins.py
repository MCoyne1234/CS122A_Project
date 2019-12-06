from gpiozero import LineSensor
from signal import pause
from gpiozero import LED


def con(RL, pinN):
   
    str = "{} Correction".format(RL)
    print(str)
    
    #print('Second thing')
    return

class wheels():
    def __init__(self):
            pass
	    
    def gogo(self):
        led0 = LED(27)
        led1 = LED(22)
        
        led0.on()
        led1.on()
        sensorL = LineSensor(4)
        sensorL.when_line = lambda: print('No line detected')
        sensorL.when_no_line = lambda: con("Left",27 )

        sensorR = LineSensor(17)
        sensorR.when_line = lambda: print('No line detected')
        sensorR.when_no_line = lambda: con("Right",22 )
        pause()

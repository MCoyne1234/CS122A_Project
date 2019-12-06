from gpiozero import LineSensor
from signal import pause

sensorL = LineSensor(4)
sensorL.when_line = lambda: print('No line detected')
sensorL.when_no_line = lambda: print('Left Correction')

sensorR = LineSensor(17)
sensorR.when_line = lambda: print('No line detected')
sensorR.when_no_line = lambda: print('Right Correction')
pause()
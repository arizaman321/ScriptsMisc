import RPi.GPIO as GPIO
from gpiozero import CPUTemperature
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
time.sleep(20)
GPIO.setup(25, GPIO.OUT, initial = GPIO.LOW) #fan initalize

def checkTemp():
    return CPUTemperature().temperature
    
while True:
    temp = checkTemp()
    print (temp)
    thresh = 45
    
    if temp > thresh:
        GPIO.output(25,GPIO.HIGH)
    
    while temp > thresh:
        time.sleep(300)
        temp = checkTemp()
        
    print ("fan off")
    GPIO.output(25,GPIO.LOW)
    time.sleep(300)
    
    




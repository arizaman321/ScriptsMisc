import RPi.GPIO as GPIO
from gpiozero import CPUTemperature
import time
while True:
    temp = CPUTemperature().temperature
    print (temp)
    time.sleep(5)


#while True:
 #   temp = CPUTemperature().temperature
  #  print (temp)
    #if temp > 45:
     #   print ("fan on")
      #  GPIO.output(25,GPIO.HIGH)
       # time.sleep(200)
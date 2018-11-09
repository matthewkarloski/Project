import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BCM)

#put all the leds in a list
leds = [5, 6, 12, 16, 18, 19, 20, 21, 22, 23]

#setup all the leds
GPIO.setup(leds, GPIO.OUT)

#setup the button
button = 25
GPIO.setup(button, GPIO.IN)
GPIO.setup(button, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(button, GPIO.IN, pull_up_down = GPIO.PUD_UP)

#put them all in a pattern that keeps going
def pattern10():
    #make sure all lights are off to start
    GPIO.output(leds, GPIO.LOW)

    #keep checking
    while(GPIO.input(button) == GPIO.HIGH):

        sleep(.1)
        GPIO.output(leds, GPIO.LOW)

        #check if someone is holding the button down, if yes, do the pattern
        if (GPIO.input(button) == GPIO.LOW):
            #turn on the first 3 lights
            GPIO.output(18, GPIO.HIGH)
            GPIO.output(19, GPIO.HIGH)
            GPIO.output(20, GPIO.HIGH)
            
        while(GPIO.input(button) == GPIO.LOW):
            sleep(.1)
            GPIO.output(21, GPIO.HIGH)
            GPIO.output(18, GPIO.LOW)
            if (GPIO.input(button) == GPIO.HIGH):
                break
            sleep(.1)
            GPIO.output(22, GPIO.HIGH)
            GPIO.output(19, GPIO.LOW)
            if (GPIO.input(button) == GPIO.HIGH):
                break
            sleep(.1)
            GPIO.output(6, GPIO.HIGH)
            GPIO.output(20, GPIO.LOW)
            if (GPIO.input(button) == GPIO.HIGH):
                break
            sleep(.1)
            GPIO.output(12, GPIO.HIGH)
            GPIO.output(21, GPIO.LOW)
            if (GPIO.input(button) == GPIO.HIGH):
                break
            sleep(.1)
            GPIO.output(23, GPIO.HIGH)
            GPIO.output(22, GPIO.LOW)
            if (GPIO.input(button) == GPIO.HIGH):
                break
            sleep(.1)
            GPIO.output(16, GPIO.HIGH)
            GPIO.output(6, GPIO.LOW)
            if (GPIO.input(button) == GPIO.HIGH):
                break
            sleep(.1)
            GPIO.output(5, GPIO.HIGH)
            GPIO.output(12, GPIO.LOW)
            if (GPIO.input(button) == GPIO.HIGH):
                break
            sleep(.1)
            GPIO.output(18, GPIO.HIGH)
            GPIO.output(23, GPIO.LOW)
            if (GPIO.input(button) == GPIO.HIGH):
                break
            sleep(.1)
            GPIO.output(19, GPIO.HIGH)
            GPIO.output(16, GPIO.LOW)
            if (GPIO.input(button) == GPIO.HIGH):
                break
            sleep(.1)
            GPIO.output(20, GPIO.HIGH)
            GPIO.output(5, GPIO.LOW)
        
pattern10()

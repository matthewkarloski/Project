###################################################################################
#Name: Matthew Karloski, Dawson Belk, Assiya Kalykova
#Date: 11/12/18
#Description: Makes a smart doorbell, once started, checks for movement or press
#           of doorbell, then sounds the right sound, then pops up a menu for the
#           user to use, then after a certain amount of time, the window closes,
#           and starts the process all over again
################################################################################


#put them all in a pattern that keeps going
def Doorbell2():
    #make sure all lights are off to start
    GPIO.output(leds, GPIO.LOW)
    
    #keep checking that the doorbell hasn't been pressed yet
    while(GPIO.input(doorbell) == GPIO.HIGH):
        
        sleep(.1)
        #make sure all the lights are off
        GPIO.output(leds, GPIO.LOW)

        
        #if someone is holding doorbell down or a movement is spotted by the sensor,
        #turn on the camera
        if (GPIO.input(doorbell) == GPIO.LOW or pir.wait_for_motion()):
            global camera
            startcamera(camera)

            #if someone was holding down the doorbell, play the doorbell and
            #play lightpattern
            if (GPIO.input(doorbell) == GPIO.LOW):
                pygame.mixer.music.load("Door bell.mp3")
                pygame.mixer.music.play()
                lightpattern()
            #else, motion sensor went off, and go to start_timer function
            else:
                start_timer(10)

            #wait for 10 seconds, to allow user to see the person, then stop the camera and go
            #to the menu
            sleep(10)
            stopcamera(camera)
            create1st()
            return ""

def start_timer(n):
    #start the timer for a designated time, then every second in that
    for i in range(n):
        sleep(1)

        #check to see if the doorbell has been pressed, and if so, play the doorbell and exit method.
        if (GPIO.input(doorbell) == GPIO.LOW):
            pygame.mixer.music.load("Door bell.mp3")
            pygame.mixer.music.play()
            lightpattern()
            return ""

    #Else, sound the alarm and scare off the intruder
    pygame.mixer.music.load("submarine-diving-alarm-daniel_simon.mp3")
    pygame.mixer.music.play()                     
        

def lightpattern():
    
    #turn on the first 3 lights
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(19, GPIO.HIGH)
    GPIO.output(20, GPIO.HIGH)

    #while the doorbell is being pressed, keep it in the loop
    while(GPIO.input(doorbell) == GPIO.LOW):
        sleep(.1)
        GPIO.output(21, GPIO.HIGH)
        GPIO.output(18, GPIO.LOW)

        #check and see if the doorbell has been unpressed
        if (GPIO.input(doorbell) == GPIO.HIGH):
            break

        #continue doing this until the doorbell has been unpressed
        
        sleep(.1)
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(19, GPIO.LOW)

        if (GPIO.input(doorbell) == GPIO.HIGH):
            break
        
        sleep(.1)
        GPIO.output(6, GPIO.HIGH)
        GPIO.output(20, GPIO.LOW)

        if (GPIO.input(doorbell) == GPIO.HIGH):
            break
        
        sleep(.1)
        GPIO.output(12, GPIO.HIGH)
        GPIO.output(21, GPIO.LOW)

        if (GPIO.input(doorbell) == GPIO.HIGH):
            break
        
        sleep(.1)
        GPIO.output(23, GPIO.HIGH)
        GPIO.output(22, GPIO.LOW)

        if (GPIO.input(doorbell) == GPIO.HIGH):
            break
        
        sleep(.1)
        GPIO.output(16, GPIO.HIGH)
        GPIO.output(6, GPIO.LOW)

        if (GPIO.input(doorbell) == GPIO.HIGH):
            break
        
        sleep(.1)
        GPIO.output(5, GPIO.HIGH)
        GPIO.output(12, GPIO.LOW)

        if (GPIO.input(doorbell) == GPIO.HIGH):
            GPIO.output(leds, GPIO.LOW)
            break
        
        sleep(.1)
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(23, GPIO.LOW)

        if (GPIO.input(doorbell) == GPIO.HIGH):
            break
        
        sleep(.1)
        GPIO.output(19, GPIO.HIGH)
        GPIO.output(16, GPIO.LOW)

        if (GPIO.input(doorbell) == GPIO.HIGH):
            break
        
        sleep(.1)
        GPIO.output(20, GPIO.HIGH)
        GPIO.output(5, GPIO.LOW)

    
    #turn off all the lights when over
    GPIO.output(leds, GPIO.LOW)


#start the camera
def startcamera(camera):
    camera.start_preview()


#stop the camera
def stopcamera(camera):
    camera.stop_preview()

#play the camera for 10 seconds 
def play():
    startcamera(camera)
    sleep(10)
    stopcamera(camera)
    
#record video for 10 seconds
def record():
    global camera
    startcamera(camera)
    camera.start_recording("/home/pi/video.h264")
    sleep(10)
    camera.stop_recording()
    stopcamera(camera)

#sound the alarm
def alarm():
    pygame.mixer.music.load("submarine-diving-alarm-daniel_simon.mp3")
    pygame.mixer.music.play()


#destroy the user menu, change the start app size to a smaller size
def Exit():
    two.destroy()
    button.config(width = 0, height = 0)
    Doorbell2()

#do nothing
def doFUCKINGnothing():
    return


#starts a timer for 4 minutes, once done, do the Exit method
def gogo():
    t = Timer(240, Exit)
    t.start()


#creates the user menu
def create1st():
    global two
    two=Tk()
    two.title("Security Menu")
    
    #make a standerdized font
    changef = tkFont.Font(family='Helvetica', size=50)

    #make the Play, Record, Alarm, and Exit buttons
    b1= Button(two, text = "View", font= changef, command=play, fg="black", bg="green", width= 15, height = 9)
    b1.grid(row=0, column=0)
    b2= Button(two, text = "Record",font= changef, command=record, fg="black", bg="white", width= 15, height = 9)
    b2.grid(row=1, column=0)
    b3= Button(two, text = "Alarm",font= changef, command=alarm, fg="black", bg="red", width= 15, height = 9)
    b3.grid(row=0, column=1)
    b4= Button(two, text = "Exit Menu",font= changef, command= Exit, fg="red", bg="black", width= 15, height = 9)
    b4.grid(row=1, column=1)

    #starts the timer
    gogo()

    #make it run until it closes
    two.mainloop()

################################################################################################
#main body of the program
import RPi.GPIO as GPIO
from time import sleep
from Tkinter import *
import pygame
from picamera import PiCamera
from threading import Timer
import tkFont
from gpiozero import MotionSensor

#setup the GPIO
GPIO.setmode(GPIO.BCM)


#put all the leds in a list
leds = [5, 6, 12, 16, 18, 19, 20, 21, 22, 23]

#setup all the leds
GPIO.setup(leds, GPIO.OUT)
pygame.mixer.init()

#setup the doorbell button
doorbell = 25
GPIO.setup(doorbell, GPIO.IN)
GPIO.setup(doorbell, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(doorbell, GPIO.IN, pull_up_down = GPIO.PUD_UP)

#setup the camera and motion sensor
camera = PiCamera()
pir = MotionSensor(26)


#creates the starting Tk window that will start the app once pressed
one =Tk()
one.title("Security")
global button
button =Button(one, text = "Start App", command = Doorbell2, fg ="white", bg="black", width = 25, height = 16)
button.grid(row = 0, column = 0)

#keep it going until it is closed
one.mainloop()

import RPi.GPIO as GPIO
from time import sleep
from Tkinter import *
import tkMessageBox
import pygame
from picamera import PiCamera
from threading import Timer
import tkFont
import tkMessageBox

GPIO.setmode(GPIO.BCM)

#put all the leds in a list
leds = [5, 6, 12, 16, 18, 19, 20, 21, 22, 23]

#setup all the leds
GPIO.setup(leds, GPIO.OUT)
pygame.mixer.init()

#setup the button
doorbell = 25
GPIO.setup(doorbell, GPIO.IN)
GPIO.setup(doorbell, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(doorbell, GPIO.IN, pull_up_down = GPIO.PUD_UP)

camera = PiCamera()

#put them all in a pattern that keeps going
def Exitdoorbell():
    global a
    a = False
    print "hi"
    exitwindow.destroy()
    
def Doorbell():
    #make sure all lights are off to start
    GPIO.output(leds, GPIO.LOW)
    global a
    a = True
    #keep checking
    while(GPIO.input(doorbell) == GPIO.HIGH and a == True):

        sleep(.1)
        GPIO.output(leds, GPIO.LOW)
        global exitwindow
        exitwindow = Tk()
        exbutton = Button(exitwindow, text = "Exit",font= changef, command= Exitdoorbell, fg="red", bg="black", width= 15, height = 9)
        exbutton.grid(row=0, column=0)
        #check if someone is holding the button down, if yes, start camera, play
        #doorbell, do the light pattern, and 10 seconds after they 
        if (GPIO.input(doorbell) == GPIO.LOW):
            global camera
            startcamera(camera)
            pygame.mixer.music.load("Door bell.mp3")
            pygame.mixer.music.play()
            lightpattern()
            sleep(10)
            stopcamera(camera)
        
        
        
    print "hello"

def Doorbell2():
    try:
        #make sure all lights are off to start
        GPIO.output(leds, GPIO.LOW)
        #keep checking
        while(GPIO.input(doorbell) == GPIO.HIGH):

            sleep(.1)
            GPIO.output(leds, GPIO.LOW)
            #check if someone is holding the button down, if yes, start camera, play
            #doorbell, do the light pattern, and 10 seconds after they 
            if (GPIO.input(doorbell) == GPIO.LOW):
                global camera
                startcamera(camera)
                pygame.mixer.music.load("Door bell.mp3")
                pygame.mixer.music.play()
                lightpattern()
                sleep(10)
                stopcamera(camera)
                return ""
    except KeyboardInterrupt:
        return ""

def lightpattern():
    
    #turn on the first 3 lights
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(19, GPIO.HIGH)
    GPIO.output(20, GPIO.HIGH)
            
    while(GPIO.input(doorbell) == GPIO.LOW):
        sleep(.1)
        GPIO.output(21, GPIO.HIGH)
        GPIO.output(18, GPIO.LOW)
        if (GPIO.input(doorbell) == GPIO.HIGH):
            break
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

    GPIO.output(leds, GPIO.LOW)


#create1st()
#me.mainloop()


#Camera testing
        
#def quit():
    #global Camera_window
    #global camera
    #Camera_window.destroy()
    #camera.stop_preview()
    
def startcamera(camera):
    camera.start_preview(alpha = 220)

def stopcamera(camera):
    camera.stop_preview()

########################################################
one =Tk()
global button

def fastquit(window, camera):
    camera.stop_recording()
    Camerawindow.destroy()
    camera.stop_preview()

def create2nd(word,r,c):
    go = Toplevel(me)
    button = Button(me, text = word, command = stop).grid(row = r, column = c)
    
def play():
    pass
    

def record():
    global camera
    startcamera(camera)
    camera.start_recording("/home/pi/Desktop/video.h264")
    sleep(10)
    camera.stop_recording()
    stopcamera(camera)

def alarm():
    pygame.mixer.music.load("submarine-diving-alarm-daniel_simon.mp3")
    pygame.mixer.music.play()

def Exit():
    two.destroy()

def create1st():
    global two
    two=Tk()
    global changef
    changef = tkFont.Font(family='Helvetica', size=50)
    b1= Button(two, text = "Play", font= changef, command=play, fg="black", bg="green", width= 15, height = 9)
    b1.grid(row=0, column=0)
    b2= Button(two, text = "Record",font= changef, command=record, fg="black", bg="white", width= 15, height = 9)
    b2.grid(row=1, column=0)
    b3= Button(two, text = "Alarm",font= changef, command=alarm, fg="black", bg="red", width= 15, height = 9)
    b3.grid(row=0, column=1)
    b4= Button(two, text = "Exit",font= changef, command= Exit, fg="red", bg="black", width= 15, height = 9)
    b4.grid(row=1, column=1)
    b5= Button(two, text = "Doorbell on",font= changef, command= Doorbell2, fg="red", bg="black", width= 15, height = 9)
    b5.grid(row=1, column=2)
    
    two.mainloop



try:
    button =Button(one, text = "Start App", command = create1st, fg ="white", bg="black", width = 25, height = 16)
    button.grid(row = 0, column = 0)
    one.mainloop()
except:
    pass

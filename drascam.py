#Does video capture and flashes LED - 12Jul16

import picamera
import subprocess
import RPi.GPIO as GPIO
import time
from time import sleep


#Variables
widtH = 640
heigH = 480
timestr = time.strftime("%Y%m%d-%H%M%S")

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
sleep(5)
#adding debounce code that will wait to see a falling edge before continuing code
GPIO.wait_for_edge(13, GPIO.FALLING, bouncetime=500)
#GPIO.cleanup(23)
 
#Do LED Flash for several times
for x in range(15):
    GPIO.output(17,0) #LED On
    sleep(.25)
    GPIO.output(17,1) #LED Off
    sleep(.15)
  
    
#Start of Video Recordings
with picamera.PiCamera() as cam:
    cam.resolution = (widtH, heigH)
    cam.start_preview()
    sleep(2)
    cam.start_recording('/home/pi/'+timestr+'video.h264')
    while True:
        input_state = GPIO.input(13)
        if input_state == False:
            cam.stop_recording()
            cam.stop_preview()
cam,stop_recording()
cam.stop_preview()
GPIO.cleanup()
exit()

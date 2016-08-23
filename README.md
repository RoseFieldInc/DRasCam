# DRasCam
Python code for controlling a Raspberry Pi to start and stop recording video with a button push.
The code uses the following Raspberry Pi model 2B+ GPIO:
GPIO#13 - Pushbutton switch (input)
GPIO#17 - LED (output)
Pi Camera - camera port

After button push, the camera begins recording video from Pi Camera. The video is stored on the Raspberry Pi in the following file format: /home/pi/YYYYMMDD-HHmmSSvideo.h264.

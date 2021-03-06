# GoPro should be connected via wifi
# make sure the 2.4ghz connection is selected and connect via the computer's wifi

from goprocam import GoProCamera, constants #imports GoPro capabilities
gpCam = GoProCamera.GoPro()

from sys import exit

import time

def video(): # defines video acquisition function 
    gpCam.shoot_video(30) # shoots 30 second video for tracking 
    v = time_stamp()
    video_stamp.append(v)
    print video_stamp

def stimulate():
    import u3 # Open the first found LabJack U3
    vibrator = u3.U3() # defines vibrator variable as u3 labjack
    FIO4_STATE_REGISTER = 6004 # defines which connection will be used to deliver power to vibrator
    vibrator.writeRegister(FIO4_STATE_REGISTER, 1) # Deliver voltage to FIO4 to power the vibrator
    time.sleep(0.15) # wait for 0.15 seconds, the length of the stimulus vibration
    t = time_stamp()
    stim_stamp.append(t)
    print stim_stamp
    vibrator.writeRegister(FIO4_STATE_REGISTER, 0) # Deliver voltage to FIO4 to power the vibrator

global start_timer # makes the variable global 
start_timer = time.time()
end_timer = start_timer + 3600 # this is when the experiment should stop running
print start_timer


def time_stamp(): # this function is used to get time stamps for stimuli presentations & videos
    elapsed_time = time.time() - start_timer
    return elapsed_time


stim_stamp = [] # creates an empty list vector to store time stamps of stimulus presentations
video_stamp = [] # creates an empty list vector to store time stamps of videos


def start(): # this function runs the actual experiment
    while round(end_timer - time.time()) > 0: # creates a timer using a while loop
        video() # calls on the GoPro to take a video

        time.sleep(150) # 2.5 minute wait before stimulus

        stimulate() # u3 labjack delivers power to vibrator to reset schooling pattern

        time.sleep(150) # 2.5 minute wait before repeating the loop

start()

print stim_stamp # prints vector with stimuli presentation time stamps
print video_stamp # prints vector with video time stamps

gpCam.downloadAll()

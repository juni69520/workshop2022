import time
import string    
import random
import webcamDetect
import modal

modal.Modal().modalYesNo()

ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10)) 
WebcamDetect = webcamDetect.WebcamDetect()

WebcamDetect.takePicture(ran, 'daily')

while True:
    for app in WebcamDetect.getActiveApps():
        if 'Teams.exe' in app:
            WebcamDetect.takePicture(ran, 'meeting')
    print("---")
    time.sleep(1)
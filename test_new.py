#!/usr/bin/env python3
# This script is an adaption of the servo_demo.py script for the AIY voice HAT, optimized for the AIY MeArm, as described in instructables: Version 1.0, 
# 2018-01-21
import aiy.audio 
import aiy.cloudspeech 
import aiy.voicehat 
from gpiozero import AngularServo
#from gpiozero import Button #activate if required from gpiozero import LED #activate if required
from time import sleep # can be required for complex procedures 
lingua = "en-GB" #sets language here: either en-GB or en-US; for all others change text as well 
vol = 30 #sets volume 
pit = 150 #sets pitch 
def order_incomplete():
  print ('order incomplete or not recognized')
  aiy.audio.say("incomplete order, please repeat!", lang=lingua, volume=vol, pitch=pit) # asking for orders def all_center():
  print("move all servos to resting positions")
  s0= s0center
  s1= s1center
  s2= s2center
  s4= s4center
  servo0 = s0
  servo1 = s1
  servo2 = s2
  # servo4 = s4
def main():
    
 recognizer = aiy.cloudspeech.get_recognizer()
 # define expected phrases
 recognizer.expect_phrase('right')
 recognizer.expect_phrase('left')
 recognizer.expect_phrase('upward')
 recognizer.expect_phrase('down')
 recognizer.expect_phrase('forward')
 recognizer.expect_phrase('back')
 recognizer.expect_phrase('maximum')
 recognizer.expect_phrase('center')
 recognizer.expect_phrase('five')
 recognizer.expect_phrase('eleven')
 recognizer.expect_phrase('twenty')
 recognizer.expect_phrase('grip')
 recognizer.expect_phrase('open')
 recognizer.expect_phrase('close')
 recognizer.expect_phrase('banana pie')
 recognizer.expect_phrase('all center')
 recognizer.expect_phrase('macro one')
 recognizer.expect_phrase('LED on')
 recognizer.expect_phrase('LED off')
 recognizer.expect_phrase('goodbye')
# set base settings to protect servos
 #Servo0 left and right
 s0max = 45 # maximum value
 s0min = -45 # minimum value
 s0center = 0 # resting position, may or may not be 0
 s0 = s0center # starting position
 #Servo1 up and down
 s1max = 20 # maximum value
 s1min = -40 # minimum value
 s1center = -10 # resting position, may or may not be 0
 s1 = s1center # starting position
 #Servo2 forward and backward
 s2max = 60 # maximum value
 s2min = -45 # minimum value
 s2center = 0 # resting position, may or may not be 0
 s2 = s2center # starting position
 #Servo4 grip
 s4max = 80 # maximum value
 s4min = 0 # minimum value
 s4center = 50 # resting position, may or may be not 0
 s4 = s4center
 # define devices
 button = aiy.voicehat.get_button() # change Button status
 led = aiy.voicehat.get_led() # change Button-LED status
 
 servo0 = AngularServo(26, initial_angle=s0center,min_angle=s0min,max_angle=s0max) # 1st connector, GPIO 26 # left and right
 servo1 = AngularServo( 6, initial_angle=s1center,min_angle=s1min,max_angle=s1max) # 2nd connector, GPIO 6 # up and down
 servo2 = AngularServo(13, initial_angle=s2center,min_angle=s2min,max_angle=s2max) # 3rd connector, GPIO 13 # for and back
 servo4 = AngularServo(12, initial_angle=s4center,min_angle=s4min,max_angle=s4max) # 5st connector, GPIO 12 # grip
# servo5 = AngularServo(24, min_angle=-45,max_angle=45) # 6th connector, GPIO 24
 
# led0 = LED(24) # LEDs are connected to servo5/GPIO 24 distance= Button(5) # distance sensor connected to servo3/GPIO 05
 # start the voice recognition procedure
 aiy.audio.get_recorder().start()
 aiy.audio.say("Hello!", lang=lingua, volume=vol, pitch=pit)
 aiy.audio.say("To start, push the blue button", lang=lingua, volume=vol, pitch=pit)
 while True:
    print("s0= ", s0, " s1= ", s1, " s2= ", s2, " s4= ", s4) # current servo values
    print()
    print("To activate voice recognition, push the blue button, then speak")
    print()
    print('Expected keywords are:')
    print(' upwards/down/forward/backwards/left/right; in combination with')
    print(' Maximum/Center/five/eleven/twenty ')
    print(' plus ')
    print(' grip open/close/center, LED on/off and goodbye.')
    print('In case use neutral words before or within phrases, as "move left to center"')
    led.set_state(aiy.voicehat.LED.ON) # LED on Button -> on: press here
    button.wait_for_press ()
    led.set_state(aiy.voicehat.LED.BLINK) # LED on Button -> blink while "listen and think"
    print('Listening...')
    aiy.audio.say("What now?", lang=lingua, volume=vol, pitch=pit) # asking for orders
    text = recognizer.recognize().lower() # recognized text, converted to lower case
    led.set_state(aiy.voicehat.LED.OFF) # LED on Button -> off
    if text is None:
       aiy.audio.say('Sorry, I did not hear you.', lang=lingua, volume=vol, pitch=pit)
    else:
        print('You said "', text, '"') # Let you check the systems interpretation
        if 'all center' in text:
          s0= s0center
          s1= s1center
          s2= s2center
          s4= s4center
          servo0 = s0
          servo1 = s1
          servo2 = s2
          servo4 = s4
        # servo 0: right and left
        elif (('right' in text) or ('write' in text)): # as "right eleven" gives "write 11"
 
          if 'maximum' in text:
            print('Moving servo0 to minimum position')
            s0 = s0min
            servo0.angle=s0
          elif ('center' in text): # move to center/resting position
             print('Moving servo0 to center position')
             s0 = s0center
             servo0.angle=s0
 
          elif (('five' in text) or ('5' in text)):
            print('Moving servo0 minus 5°')
            s0t=s0-5 # substract 5 from value
            if (s0t < s0min): s0=s0min # must not go above maximum or minimum
            else: s0=s0t
            servo0.angle=s0
          elif (('eleven' in text) or ("11" in text)):
            print('Moving servo0 minus 11°')
            s0t=s0-11 # substract 11 from value
            if (s0t < s0min): s0=s0min # must not go above maximum or minimum
            else: s0=s0t
            servo0.angle=s0
          elif (('twenty' in text) or ("20" in text)):
            print('Moving servo0 minus 20°')
            s0t=s0-20 # substract 20 from value
            if (s0t < s0min): s0=s0min # must not go above maximum or minimum
            else: s0=s0t
            servo0.angle=s0
          else:
            order_incomplete()
             
        elif 'left' in text:
          if ('maximum' in text):
            print('Moving servo0 to maximum position')
            s0 = s0max
            servo0.angle=s0
          elif ('center' in text): # move to center/resting position
             print('Moving servo0 to center position')
             s0 = s0center
             servo0.angle=s0
          elif (('five' in text) or ('5' in text)):
            print('Moving servo0 plus 5°')
            s0t=s0+5 # add 5 to value
            if (s0t > s0max): s0=s0max # must not go above maximum or minimum
            else: s0=s0t
            servo0.angle=s0
          elif (('eleven' in text) or ('11' in text)):
            print('Moving servo0 plus 11°')
            s0t=s0+11 # add 11 to value
            if (s0t > s0max): s0=s0max # must not go above maximum or minimum
            else: s0=s0t
            servo0.angle=s0
          elif (('twenty' in text) or ("20" in text)):
            print('Moving servo0 plus 20°')
            s0t=s0+20 # add 20 to value
            if (s0t > s0max): s0=s0max # must not excede maximum or minimum
            else: s0=s0t
            servo0.angle=s0
          else:
            order_incomplete()
        # servo 1: up and down
        elif ('down' in text):
 
          if 'maximum' in text:
            print('Moving servo1 to minimum position')
            s1 = s1min
            servo1.angle=s1
          elif ('center' in text): # move to center/resting position
             print('Moving servo1 to center position')
             s1 = s1center
             servo1.angle=s1
 
          elif (('five' in text) or ('5' in text)):
            print('Moving servo1 minus 5°')
            s1t=s1-5 # substract 5 from value
            if (s1t < s1min): s1=s1min # must not go above maximum or minimum
            else: s1=s1t
            servo1.angle=s1
          elif (('eleven' in text) or ("11" in text)):
            print('Moving servo1 minus 11°')
            s1t=s1-11 # substract 11 from value
            if (s1t < s1min): s1=s1min # must not go above maximum or below minimum
            else: s1=s1t
            servo1.angle=s1
          elif (('twenty' in text) or ("20" in text)):
            print('Moving servo1 minus 20°')
            s1t=s1-20 # substract 20 from value
            if (s1t < s1min): s1=s1min # must not excede maximum or minimum
            else: s1=s1t
            servo1.angle=s1
          else:
            order_incomplete()
             
        elif 'up' in text:
          if ('maximum' in text):
            print('Moving servo1 to maximum position')
            s1 = s1max
            servo1.angle=s1
          elif ('center' in text): # move to center/resting position
             print('Moving servo1 to center position')
             s1 = s1center
             servo1.angle=s1
          elif (('five' in text) or ('5' in text)):
            print('Moving servo1 plus 5°')
            s1t=s1+5 # add 5 to value
            if (s1t > s1max): s1=s1max # must not go above maximum or minimum
            else: s1=s1t
            servo1.angle=s1
          elif (('eleven' in text) or ('11' in text)):
            print('Moving servo1 plus 11°')
            s1t=s1+11 # add 11 to value
            if (s1t > s1max): s1=s1max # must not go above maximum or minimum
            else: s1=s1t
            servo1.angle=s1
          elif (('twenty' in text) or ("20" in text)):
            print('Moving servo1 plus 20°')
            s1t=s1+20 # add 20 to value
            if (s1t > s1max): s1=s1max # must not excede maximum or minimum
            else: s1=s1t
            servo1.angle=s1
          else:
            order_incomplete()
        # Servo 2: forwards and back
        elif ('back' in text):
 
          if 'maximum' in text:
            print('Moving servo2 to minimum position')
            s2 = s2min
            servo2.angle=s2
          elif ('center' in text): # move to center/resting position
             print('Moving servo2 to center position')
             s2 = s2center
             servo2.angle=s2
 
          elif (('five' in text) or ('5' in text)):
            print('Moving servo2 minus 5°')
            s2t=s2-5 # substract 5 from value
            if (s2t < s2min): s2=s2min # must not go above maximum or minimum
            else: s2=s2t
            servo2.angle=s2
          elif (('eleven' in text) or ("11" in text)):
            print('Moving servo2 minus 11°')
            s2t=s2-11 # substract 11 from value
            if (s2t < s2min): s2=s2min # must not go above maximum or below minimum
            else: s2=s2t
            servo2.angle=s2
          elif (('twenty' in text) or ("20" in text)):
            print('Moving servo2 minus 20°')
            s2t=s2-20 # substract 20 from value
            if (s2t < s2min): s2=s2min # must not excede maximum or minimum
            else: s2=s2t
            servo1.angle=s2
          else:
            order_incomplete()
             
        elif ('for' in text):
          if ('maximum' in text):
            print('Moving servo1 to maximum position')
            s2 = s2max
            servo2.angle=s2
          elif ('center' in text): # move to center/resting position
             print('Moving servo2 to center position')
             s2 = s2center
             servo2.angle=s2
          elif (('five' in text) or ('5' in text)):
            print('Moving servo2 plus 5°')
            s2t=s2+5 # add 5 to value
            if (s2t > s2max): s2=s2max # must not go above maximum or minimum
            else: s2=s2t
            servo1.angle=s2
          elif (('eleven' in text) or ('11' in text)):
            print('Moving servo2 plus 11°')
            s2t=s2+11 # add 11 to value
            if (s2t > s2max): s2=s2max # must not go above maximum or minimum
            else: s2=s2t
            servo1.angle=s2
          elif (('twenty' in text) or ("20" in text)):
            print('Moving servo2 plus 20°')
            s2t=s2+20 # add 20 to value
            if (s2t > s2max): s2=s2max # must not excede maximum or minimum
            else: s2=s2t
            servo1.angle=s2
          else:
            order_incomplete()
 
        # Servo 4: grip
        elif ('grip' in text):
          if 'open' in text:
            print('Moving servo4 to maximum position')
            s4= s4min
            servo4.angle=s4
          elif (('close' in text) or ('clothes' in text)): # common recognition error
            print('Moving servo4 to minimum position')
            s4= s4max
            servo4.angle=s4
          elif 'center' in text:
             print('Moving servo4 to middle position')
             s4=s4center
             servo4.angle=s4
          else: order_incomplete()
        elif "macro one" in text:
          print("starting macro1")
          s0= 45 # move to right
          s1= 20 # move
          s2= -10
          s4= 45
          servo0 = s0
          servo1 = s1
          servo2 = s2
          servo4 = s4
          
          sleep (2)
          s4=90 #close grip
          servo4=s4
          sleep(1)
         
          s0= -40 # move to left
          s1= -20
          s2= 10
          s4= 45
          servo0 = s0
          servo1 = s1
          servo2 = s2
          sleep (2)
          s4=45 # open grip
          servo4=s4
         
          
        # LED
        elif 'LED off' in text:
             print ('switching off button LED')
             led.set_state(aiy.voicehat.LED.OFF)
        elif 'LED on' in text:
             print ('switching on button LED')
             led.set_state(aiy.voicehat.LED.ON)
        # goodbye
        elif 'goodbye' in text:
             aiy.audio.say("Goodbye", lang=lingua, volume=vol, pitch=pit)
             # aiy.audio.say('Arrivederci', lang="it-IT") aiy.audio.say('Auf Wiedersehen', lang="de-DE")
 
             s0= s0center
             s1= s1center
             s2= s2center
             s4= s4center
             servo0 = s0
             servo1 = s1
             servo2 = s2
             servo4 = s4
             led.set_state(aiy.voicehat.LED.OFF)
             sleep (3)
             print('bye!')
             break
        else:
             print('no front keyword recognized!')
             aiy.audio.say("Sorry, no keyword recognized! Please repeat!", lang=lingua, volume=vol, pitch=pit)
             
if __name__ == '__main__':
 main()

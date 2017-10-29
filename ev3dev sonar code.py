#!/usr/bin/env python3
import ev3dev.ev3 as ev3
from time import sleep

#devices
btn = ev3.Button()
sonar = ev3.UltrasonicSensor()
leftWheel = ev3.LargeMotor('outA')
rightWheel = ev3.LargeMotor('outD')

#parameters
fullSpeed=600

#inital_values
der=0;
integ=0;

#one_step
def turn(kp=10,kd=50,ki=0.01):
        global der, integ;
		
		#measure_the_distance
		
        distance=sonar.distance_centimeters
		
		#find_error
		
        err=distance-20
        if err>50:
                err=50
				
		#calculate proportional element
		
        P = kp * err;
		
		#calculate derivative element
		
        D = kd * (err - der)
		der=err
		
		#calculate integral element
		
        integ += err
        I = ki * integ
		
		#calculate full correction
		
        w=P+I+D;
		
		#calculate left wheel speed
		
        left=int(fullSpeed/2+w)
        if left > fullSpeed:
                left=fullSpeed
        if left<0:
                left=0
				
		#calculate right wheel speed
		
		right=fullSpeed-left
		
		#set wheel speed
		
        leftWheel.run_forever(speed_sp=left)
        rightWheel.run_forever(speed_sp=right)

#while loop

while not btn.any():
    turn()
    sleep(0.05)

#stop

leftWheel.stop()
rightWheel.stop()
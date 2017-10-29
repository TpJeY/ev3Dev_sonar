#EV3 movement along the wall by Ultrasonic sensor data with PID controller

##Description of the project

This project is designed to provide movement along the wall by Ultrasonic sensor data for Lego Mindstorm differential drive robot. Sensor provides information about current distance at each iteration, after that it is compared with given distance (which was set as 20 cm). Information about difference between desired and current distance is used to control the angular velocity by calculating speed of every wheel. Rotation speed is translated to actuators of the EV3 robot. The speed is corrected by PID controller for smooth and stable movement.

##Description of the work process

[Ev3dev](http://www.ev3dev.org/) was used as an operating system (System setup is described [here](http://www.ev3dev.org/docs/getting-started/)). Python was used as programming language ([ev3dev-lang-python](https://github.com/ev3dev/ev3dev-lang-python)  was used). Bluetooth connection was used for communication with robot (bluetooth setup is described [here](http://www.ev3dev.org/docs/tutorials/connecting-to-the-internet-via-bluetooth/)). Finally SSH was used for connection and to run scripts on robot (setup is described [here](http://www.ev3dev.org/docs/tutorials/connecting-to-ev3dev-with-ssh/)).

##Explanation of the result values

The constants for PID controller were chosen during the number of physical tests. The transition process was evaluated by the characteristic features of this process (response time, overshooting, steady-state error).

##Explanation why these values are the best

Firstly the value of P coefficient was chosen to correspond to the real values, than D coefficient was chosen by the response time and finally the I coefficient was chosen by the scale of movement smoothness.

##Link to YouTube video

[Here](https://www.youtube.com/watch?v=ip0MgYu2i68)

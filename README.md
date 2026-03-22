[HORIZON SOFTWARE SUBTEAM TASKS]

ANAINA VIBIN S2


[Level 1]
Open the file program.py in GitHub Codespace and click run.
It will ask for coordinates of origin and destination.
Afterwards the initial velocity, acceleration and maximum velocity it can reach.
The output is the distance it needs to travel and the time taken to reach the destination coordinates.
Error handling for cases where acceleration is equal to zero or negative and initial speed is zero is taken into account.



[Level 2]
The video attached anainavibin_horizon_software_tinkercad.mp4 shows the working of the simulation.
The file servo_motor1.ino contains the source code used to program the Arduino UNO microcontroller.
The program puts a restraint to how much angle a servo motor can rotate, in this case it is maximum of 68 degrees.
A potentiometer is used to determine the angle at which the servo motor must turn.
If the potentiometer knob is turned more than 68 degrees an led lights up as a warning.

Link to the tinkercad: https://www.tinkercad.com/things/3R80aYqtg1p-servo-motor?sharecode=t80PSd2s-uqAS-Sd6-jinmVwV4xdZ3xofr_esWhZcUw
Go to the provided link and click "Simulate" and then click "Start Simulation" to run the simulation.
Turn the knob of potentiometer to turn the servo motor.
Click "Code" to see the source code of Arduino UNO.

[Level 3]
  
  Install Ubuntu 22.04 version and then install ROS2
  Refer to the links below for installation 
  ROS2:   https://docs.ros.org/en/humble/index.html
  Ubuntu 22.04: https://releases.ubuntu.com/jammy/

  For Environment setup:
  $ source /opt/ros/humble/setup.bash
  

  Make sure both the files sensor_node.py and subscriber_node.py in Level 3 folder is saved to the rover_control file in the workspace.
  In setup.py add configuration update
    entry_points={
      'console_scripts': \[
        'sensor_node = rover_control.sensor_node:main',
        'subscriber_node = rover_control.subscriber_node:main',
      ]
    },
    
  Building the workspace:
  $ cd~/rover_workspace
  $ colcon build
  $ source install/setup.bash
  

  In terminal 1, to run the publisher node:
  $ ros2 run rover_control sensor_node

  In terminal 2 to run the subscriber node:
  $ ros2 run rover_control subscriber_node


  Both of these running together will show the output similar to image Nodes.png in Folder Level 3.
  
  In here one node (publisher node) is receiving data (in this case the distance) and the subscriber node prints it in the terminal.
  
  Images ubuntu1.png and ubuntu2.png show the installation of Ubuntu 22.04 as a virtual machine in Oracle VirtualBox.
  
  Images ros2.png and ros2_2.png show the installation of ros2 in the virtual machine with Ubuntu 22.04.
  
  
    
  

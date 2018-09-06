# MHP_BL_Testing

This repo contains code to conduct battery life testing.

To get setup and install this repo:
1. Clone this repo into the Documents folder on the pi
2. Setup the start.py script to run on boot by typing:
   a) "sudo nano /etc/rc.local"
   b) Putting the line "python /home/pi/Documents/MHP_BL_Testing/start.py &" before the line "exit 0"
   c) If running a loaded test with camera breakout, put "python /home/pi/Documents/MHP_Raspicam/Camera.py &" before the line "exit 0"
      also. Make sure the MHP_Raspicam GitHub library is also in the Documents folder on the pi, and that the camera is connected.
3. Setup the log.py script to run every minute by typing
   a) "crontab -e"
   b) Putting the line "* * * * * python /home/pi/Documents/MHP_BL_Testing/log.py" at the end of the file
   c) If running a loaded test with camera breakout, also put "*/10 * * * * sh /home/pi/Documents/MHP_BL_Testing/kill.sh" at the end of 
      the file. This will run the camera script repetitively every 10 minutes.

Note make sure that the bl_log.txt file is created using "nano bl_log.txt" instead of "sudo nano bl_log.txt" otherwise the python
scripts will not have permission to edit the file.

When setting up the test on the 7" official raspberry pi touchscreen you will need to disable screen sleep. Otherwise the battery life from the test result will be around double what it should be.

To do this 
1) run the command "sudo apt-get install xscreensaver"
2) Then open an x11vnc window using "x11vnc -display :0 -usepw -listen <INSERT_IP_ADDRESS>".
3) Then open vnc viewer on your computer, and type the ip address of the pi
4) Open a terminal window once you have loaded the desktop and type "xscreensaver"
5) From the drop down select "Disable Screen Sleep"

Some notes:
- You may have to install x11vnc using "sudo apt-get install x11vnc". This may not work if you have not run "sudo apt-get update" before.
- When adding files to the Logs directory make sure you label them correctly with sufficient detail.

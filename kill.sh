
output=$(pgrep -lf python)
process=$(echo $output | tr -dc '0-9')
sudo kill $process
sudo rm /home/pi/Documents/MHP_Raspicam/Video/*.h264
python /home/pi/Documents/MHP_Raspicam/Camera.py &

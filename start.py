# This file prints a "testing start" statement into the log file so you can 
# work out where the pi was turned on

f = open('/home/pi/Documents/MHP_BL_Testing/bl_log.txt', 'a')

f.write("\n\nPi Turned on, Restarted Testing here!\n")

f.close()

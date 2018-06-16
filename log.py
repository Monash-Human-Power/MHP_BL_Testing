# This file appends the bl_log.txt file with the current date and time each
# time the script is called.

import datetime

now = datetime.datetime.now()

f = open('/home/pi/Documents/MHP_BL_Testing/bl_log.txt', 'a')

f.write(str(now)+"\n")

f.close()

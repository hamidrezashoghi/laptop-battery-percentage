#!/usr/bin/env python3

import os
import psutil

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = str(battery.percent)
percent_int = int(float(percent))

if plugged == False and percent_int < 20:
    text = "Battery is " + str(int(float(percent))) + "%. Please plug-in your charger"
    notify = 'zenity --width=250 --warning --text "{}" --title="{}" --timeout=4'.format(text, "Battery Percentage!")
    os.system(notify)

if plugged == True and percent_int == 100:
    text = "Battery is " + str(int(float(percent))) + "%. Please unplug your charger, electricite is expensive!"
    os.system(notify)

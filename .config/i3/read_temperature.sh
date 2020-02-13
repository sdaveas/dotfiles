#!/bin/bash
rm ~/.config/i3/temp1_input
if [ ! -d "/sys/devices/platform/coretemp.0/hwmon/hwmon2" ] ; then
    ln -s /sys/devices/platform/coretemp.0/hwmon/hwmon1/temp1_input ~/.config/i3/
elif [ ! -d "/sys/devices/platform/coretemp.0/hwmon/hwmon1" ] ; then
    ln -s /sys/devices/platform/coretemp.0/hwmon/hwmon2/temp1_input ~/.config/i3/
fi

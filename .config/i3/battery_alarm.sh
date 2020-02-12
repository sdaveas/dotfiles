#!/bin/bash

threshold_1=20
threshold_2=15
threshold_3=10
threshold_4=5
declare -a thresholds=($threshold_1 $threshold_2 $threshold_3 $threshold_4)

message_1="Battery is running low."
message_2="Battery is running realy low."
message_3="Srsly, plug in the adapter."
message_4="At least :w."
declare -a messages=("$message_1" "$message_2" "$message_3" "$message_4")

current_level=`cat /sys/class/power_supply/BAT0/capacity`
echo "Current value is $current_level"

size=${#thresholds[@]}
echo "$size"
for ((i=0;i<$size;i++))
do
    threshold=${thresholds[$i]}
    while [ "$current_level" -gt "$threshold" ]
    do
        sleep 10
        current_level=`cat /sys/class/power_supply/BAT0/capacity`
        echo "Current value is $current_level"
    done;

    message="${messages[$i]}"
    if [ $i -eq "0" ]
    then
        i3-nagbar -m "$message" -t warning
    else
        i3-nagbar -m "$message"
    fi
done

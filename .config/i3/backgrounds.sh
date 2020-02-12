#!/bin/bash

if [ -f /tmp/background_deamon ]; then
    exit;
fi

echo "alive" > /tmp/background_deamon

while true; do
    for img in /home/stelios/Pictures/i3/backgrounds/daim/*
    do
        sleep 1800
        feh --bg-center "$img"
    done
done

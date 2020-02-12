#!/bin/bash
pkill -P $(ps -e | grep backgrounds.sh | awk '{print $1}') sleep

#!/bin/bash
#chmod +x temp.sh
cd /home/pi/Raspberry/
while :
do
    python3 temp-plot.py &
    sleep 30
    pidof python3 temp-plot.py > pid.txt
    cat pid.txt
    echo "plotting 24h"
    sleep 24h
    pid=$(cat pid.txt) && kill -9 $pid
    echo "killing"
    sleep 10
    dphys-swapfile swapoff
    sleep 3
    dphys-swapfile swapon
done
#$ sudo ./temp.sh

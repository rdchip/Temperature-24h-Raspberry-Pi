echo "plotting"; python3 tempsensor2.py
sleep 3; pidof python3 tempsensor2.py > pid.txt; echo "sleeping"; sleep 24h; echo "killing"; pid=$(cat pid.txt) && kill -9 $pid; dphys-swapfile swapoff; dphys-swapfile swapon

#!/bin/bash
############## This a script for connection ##########
id=$1

echo "53215404" | sudo -S mount 192.168.137.23:/home/molevision/Desktop/mmwave
echo "53215404" | sudo -S mount -t /home/ubuntu/Desktop/mmwave
echo "53215404" | sudo systemctl enable --now ssh
echo "53215404" | sudo ssh molevision@192.168.137.23 python3 /home/molevision/Desktop/mmwave/mmwave_p.py $id 


exit


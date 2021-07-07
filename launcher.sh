#!/bin/sh
#launcher.sh

cd /
cd home/pi/ceaos-picam
sudo python3 setup.py install
cd ceaos_picam
sudo python3 driver.py
cd /

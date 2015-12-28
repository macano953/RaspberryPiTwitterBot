#!/bin/bash

cat /sys/class/thermal/thermal_zone0/temp > cpuTemp
/opt/vc/bin/vcgencmd measure_temp > gpuTemp
python convert.py

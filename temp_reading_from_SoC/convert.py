#!/bin/python
#script to read a file and extract a number

fo = open("cpuTemp")
str = fo.read()
fo.close()
cpuTemp=eval(str) 
cpuTemp /=1000.00
fo = open("gpuTemp")
str2 = fo.read()
fo.close()
gpuTemp=eval(str2[5:9])

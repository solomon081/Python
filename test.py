#!/usr/bin/python3
import math
import os

from sympy import *

pi = math.pi

if math.sin(pi/3) != math.cos(pi/6):
	print "Holy Shit!"
	print math.sin(pi/3) - math.cos(pi/6)
else:
	print "oh yeah!"
#!/usr/bin/python3
import math
import os

from sympy import *

pi = math.pi

def function(trig):
	def trig():
		theta = input("trig(")
		output = math.trig(theta)
		diff = output - round(output, 10)
		if abs(output) == math.cos(math.pi/6):
			output = str(output)
			output = list(output)
			output.insert(0, " sqrt(3)/2 or ")
			print ''.join(output)
		if abs(diff) <= 0.000000000000001:
			output = round(output, 15)
		print output
arg = raw_input("Choose a trig function")
function(arg)
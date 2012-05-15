#!/usr/bin/python3
import math
import os
import sys

def cls():
	os.system(['clear','cls'][os.name == 'nt'])

from sympy import *

pi = math.pi
loop = 0
append = "false"
optionlist = ['1', '2', '3', '0', 'exit']

def cos():
	append = "false"
	theta = input("cos(")
	output = math.cos(theta)
	diff = output - round(output, 10)
	if abs(diff) <= 0.000000000000001:
		output = round(output, 10)
	if abs(output) == math.cos(math.pi/6):
		if abs(output) == output:
			output = str(output)
			output = list(output)
			output.insert(0, " sqrt(3)/2 or ")
		else:
			output = str(output)
			output = list(output)
			output.insert(0, " -sqrt(3)/2 or ")
		print ''.join(output)
		append = "true"
	elif abs(output) == 0.5:
		if abs(output) == output:
			output = str(output)
			output = list(output)
			output.insert(0, " 1/2 or ")
		else:
			output = str(output)
			output = list(output)
			output.insert(0, " -1/2 or ")
		print ''.join(output)
		append = "true"
	elif abs(output) == math.cos(pi/4):
		if abs(output) == output:
			output = str(output)
			output = list(output)
			output.insert(0, " sqrt(2)/2 or ")
		else:
			output = str(output)
			output = list(output)
			output.insert(0, " -sqrt(2)/2 or ")
		print ''.join(output)
		append = "true"
	if append not in ["true"]:
		print output

def sin():
	append = "false"
	theta = input("sin(")
	output = math.sin(theta)
	diff = output - round(output, 10)
	if abs(diff) <= 0.000000000000001:
		output = round(output, 10)
	if abs(output) == math.sin(math.pi/3):
		if abs(output) == output:
			output = str(output)
			output = list(output)
			output.insert(0, " sqrt(3)/2 or ")
		else:
			output = str(output)
			output = list(output)
			output.insert(0, " -sqrt(3)/2 or ")
		print ''.join(output)
		append = "true"
	elif abs(output) == 0.5:
		if abs(output) == output:
			output = str(output)
			output = list(output)
			output.insert(0, " 1/2 or ")
		else:
			output = str(output)
			output = list(output)
			output.insert(0, " -1/2 or ")
		print ''.join(output)
		append = "true"
	elif abs(output) == math.sin(pi/4):
		if abs(output) == output:
			output = str(output)
			output = list(output)
			output.insert(0, " sqrt(2)/2 or ")
		else:
			output = str(output)
			output = list(output)
			output.insert(0, " -sqrt(2)/2 or ")
		print ''.join(output)
		append = "true"
	if append not in ["true"]:
		print output

def tan():
	append = "false"
	theta = input("tan(")
	output = math.tan(theta)
	diff = output - round(output, 10)
	if abs(diff) <= 0.000000000000001:
		output = round(output, 10)
	if append not in ["true"]:
		print output

while loop != 1:
	raw_input("press enter to continue")
	cls()
	print "1. cos"
	print "2. sin"
	print "3. tan"
	print "0. exit"
	option = raw_input("Please make a selection\n")
	if option not in optionlist:
		print "invalid option"
	elif option == "exit":
		option = '0'
		option = eval(option)
	else:
		option = eval(option)
	if option == 1:
		cos()
	elif option == 2:			
		sin()
	elif option == 3:
		tan()
	elif option == 0:
		loop = 1
print "Goodbye\nTo quit please press enter"
raw_input()
cls()
exit()
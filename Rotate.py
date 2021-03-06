#!/usr/bin/python3
from __future__ import division
import math
import os
import sys

def cls():
	os.system(['clear','cls'][os.name == 'nt'])

#from sympy import *

pi = math.pi

def d(angle, point="", center=(0,0)):
	def roundsin(sininput):
		diff = math.sin(sininput)-round(math.sin(sininput), 10)
		if abs(diff) <= 0.000000000000001:
			output = round(math.sin(sininput), 10)
		else:
			output = math.sin(sininput)
		return output
	def roundcos(cosinput):
		diff = math.cos(cosinput)-round(math.cos(cosinput), 10)
		if abs(diff) <= 0.000000000000001:
			output = round(math.cos(cosinput), 10)
		else:
			output = math.cos(cosinput)
		return output	
	if angle == help:
		print "For help, type \"Rotate.help\""
		return
	elif center == "origin":
		center = (0,0)
	#print "point =", point
	angle = math.radians(int(angle))
	xpoint, ypoint = point
	xcenter, ycenter = center
	#print "angle =", angle
	#print "xcenter =", xcenter
	#print "ycenter =", ycenter
	#print "xpoint =", xpoint
	#print "ypoint =", ypoint
	#CALCULATION TIME
	D = 2*math.sqrt(((xpoint - xcenter)**2)+((ypoint - ycenter)**2))*roundsin(0.5*angle)
	B = math.asin((roundsin(angle)/(2*roundsin(0.5*angle))))
	A = math.atan((xpoint - xcenter)/(ypoint - xcenter))
	C = (math.pi/2) - B - A
	xdiff = D * roundcos(C)
	ydiff = D * roundsin(C)
	#print "D =", D
	#print "B =", B
	#print "A =", A
	#print "C =", C
	#print "xdiff =", xdiff
	#print "ydiff =", ydiff
	#xprime = xpoint - xcenter - (2*(math.sqrt((((xpoint - xcenter)**2)+(ypoint - ycenter)**2))*roundsin(0.5*angle)*roundcos(90-math.asin((roundsin(angle)/(2*roundsin(0.5*angle))))-math.atan((xpoint - xcenter)/(ypoint - ycenter))))) + xcenter
	xprime = xpoint - xdiff
	yprime = ypoint - ydiff
	#print "xprime =", xprime
	#print "yprime =", yprime
	if abs(xprime - round(xprime, 10)) <= 0.000000000001:
			xprime = round(xprime, 10)
	if abs(yprime - round(yprime, 10)) <= 0.000000000001:
			yprime = round(yprime, 10)
	#if yprime == -0:
	#	yprime = 0
	#if xprime == -0:
	#	xprime = 0
	if xprime == int(xprime):
		xprime = int(xprime)
	if yprime == int(yprime):
		yprime = int(yprime)
	pointprime = (xprime, yprime)
	#print pointprime
	return pointprime

def r(angle, point="", center=(0,0)):
	def roundsin(sininput):
		diff = math.sin(sininput)-round(math.sin(sininput), 10)
		if abs(diff) <= 0.000000000000001:
			output = round(math.sin(sininput), 10)
		else:
			output = math.sin(sininput)
		return output
	def roundcos(cosinput):
		diff = math.cos(cosinput)-round(math.cos(cosinput), 10)
		if abs(diff) <= 0.000000000000001:
			output = round(math.cos(cosinput), 10)
		else:
			output = math.cos(cosinput)
		return output	
	if angle == help:
		print "For help, type \"Rotate.help\""
		return
	elif center == "origin":
		center = (0,0)
	#print "point =", point
	xpoint, ypoint = point
	xcenter, ycenter = center
	#print "angle =", angle
	#print "xcenter =", xcenter
	#print "ycenter =", ycenter
	#print "xpoint =", xpoint
	#print "ypoint =", ypoint
	#CALCULATION TIME
	D = 2*math.sqrt(((xpoint - xcenter)**2)+((ypoint - ycenter)**2))*roundsin(0.5*angle)
	B = math.asin((roundsin(angle)/(2*roundsin(0.5*angle))))
	A = math.atan((xpoint - xcenter)/(ypoint - xcenter))
	C = (math.pi/2) - B - A
	xdiff = D * roundcos(C)
	ydiff = D * roundsin(C)
	#print "D =", D
	#print "B =", B
	#print "A =", A
	#print "C =", C
	#print "xdiff =", xdiff
	#print "ydiff =", ydiff
	#xprime = xpoint - xcenter - (2*(math.sqrt((((xpoint - xcenter)**2)+(ypoint - ycenter)**2))*roundsin(0.5*angle)*roundcos(90-math.asin((roundsin(angle)/(2*roundsin(0.5*angle))))-math.atan((xpoint - xcenter)/(ypoint - ycenter))))) + xcenter
	xprime = xpoint - xdiff
	yprime = ypoint - ydiff
	#print "xprime =", xprime
	#print "yprime =", yprime
	if abs(xprime - round(xprime, 10)) <= 0.000000000001:
			xprime = round(xprime, 10)
	if abs(yprime - round(yprime, 10)) <= 0.000000000001:
			yprime = round(yprime, 10)
	#if yprime == -0:
	#	yprime = 0
	#if xprime == -0:
	#	xprime = 0
	if xprime == int(xprime):
		xprime = int(xprime)
	if yprime == int(yprime):
		yprime = int(yprime)
	pointprime = (xprime, yprime)
	#print pointprime
	return pointprime

def help():
	x = 1
	while x != 0:
		print "This function gives the coordinates of a point rotated through an angle about a center of rotation."
		print "To input the angle in degrees, type \"D\"."
		print "To input the angle in radians, type \"R\"."
		selection = raw_input()
		if selection == "D":
			point = input("Choose a point to rotate:")
			print "Choose how many degrees you would like to rotate the point", point,":"
			angle = input()
			center = input("Choose a center of rotation about which to rotate:")
			if center == "":
				center = (0,0)
			x = 0
			output = D(angle, point, center)
			return output
		elif selection == "R":
			pass
		else:
			print
#angle = input("angle=")
#point = input("point=")
#Rotate(angle, point)
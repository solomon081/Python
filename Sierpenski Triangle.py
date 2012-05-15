#! /usr/bin/env python

import os

def cls():
	os.system(['clear','cls'][os.name == 'nt'])
	
wave = 0
option = 1

def shaded(wave):
	shaded.output = 3 ** wave
	return shaded.output

def unshaded(wave):
	unshaded.output = (3 ** wave - 1)/2
	return unshaded.output

def alltri(wave):
	alltri.output = unshaded(wave) + shaded(wave)
	return alltri.output

while option != 0:
	raw_input("Press \"Enter\" to continue")
	cls()
	print "\n\n\n*****MENU*****"
	print "1. Number of Right-Side Up/Shaded Triangles\n"
	print "2. Number of Upside-Down/Non-shaded Triangles\n"
	print "3. All Triangles\n"
	print "0. Quit\n"
	print "For help type \"help\"\n"
	option = raw_input("Please make a selection:\n")
	if option == 'help':
		cls()
		print """
			Sorry, figure it out.
			"""
	elif option in ['1', '2', '3', '0']:
		numop = eval(option)
		if numop == 1:
			wave = input("How many waves? (for help type \"help\")\n")
			print "There are", shaded(wave), "right-side up/shaded triangles by wave", wave
		if numop == 2:
			wave = input("How many waves? (for help type \"help\")\n")
			print "There are", unshaded(wave), "upside-down/non-shaded triangles by wave", wave
		if numop == 3:
			wave = input("How many waves? (for help type \"help\")\n")
			print "There are", alltri(wave), "triangles by wave", wave
		if numop == 0:
			raw_input("Press \"Enter\" to quit")
			break
	else:
		print "Invalid option"
cls()
exit

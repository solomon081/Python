#! /usr/bin/env python

import os

def cls():
	os.system(['clear','cls'][os.name == 'nt'])

option = 1
term_1 = 0
term_2 = 1
while option != 0:
	raw_input("\nPress \"Enter\" to Continue")
	cls()
	print "\n\n\n************MENU************"
	print "1. Counting"
	print "2. Fibonacci"
	print "0. Quit"
	option = input("Please make a selection\n")
	if option == 1:
		print "1. Counting Up"
		print "2. Counting Down"
		print "0. Quit"
		option = input("Please make a selection\n")
		if option == 1:
			end_num = input("Choose a number to which to count\n")
			interval = input("Choos a number by which to count\n")
			cls()
			for x in range(0, end_num+1, interval):
				print x
		elif option == 2:
			start_num = input("Choose a number at which to start\n")
			interval = input("Choose a number by which to count\n")
			cls()
			for x in range(start_num, -1, -1*interval):
				print x
		elif option == 0:
			break
		else:
			print "Invalid option"
	elif option == 2:
		print "1. Give a term"
		print "2. Count to a term"
		print "0. Quit"
		option = input("Please make a selection\n")
		if option == 1:
			term_num = input("Which term would you like?\n")
			cls()
			term_1 = 0
			term_2 = 1
			term_3 = 0
			while term_num != 1:
				term_3 = term_1 + term_2
				term_1 = term_2
				term_2 = term_3
				term_num = term_num-1
			print term_1
		if option == 2:
			term_num = input("How many terms of the fibonacci sequence would you like?\n")
			cls()
			term_1 = 0
			term_2 = 1
			term_3 = 0
			while term_num != 0:
				print term_1
				term_3 = term_1 + term_2
				term_1 = term_2
				term_2 = term_3
				term_num = term_num-1
		elif option == 0:
			break
		else:
			print "Invalid option"
	elif option == 0:
				print "Goodbye"
				raw_input("Press \"Enter\" to close this window")
				raise SystemExit
	else:
		print "Invalid option"   
exit

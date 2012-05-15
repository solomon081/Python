password = "triaro"

print "Guess my password!"

guess = raw_input()

if guess == password:
	print "Correct!"
	
elif guess != password:
	print "LOCKED OUT!"
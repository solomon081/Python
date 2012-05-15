num = input("choose a number")
cache = num-1
fact = 2
while cache != 1:
        if num%fact != 0:
                fact = fact+1
                cache = cache-1
                if cache == 1:
                        print "Your number is prime!"
                        break
        elif num%fact == 0:
                print "Your number is not prime! It is divisible by"
                print fact
                break

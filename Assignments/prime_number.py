'''
program to find prime number.
'''
#reading a value from the user
number = int(input("enter a number to check : "))
if number <2 :
    print "Prime numbers start from number 2"
if number == 2:
    print str(number) + " is a prime number"
else:
    for i in range(2,number):
        if number % i == 0:
            print str(number) + " is not a prime number"
            break
        else:
            print str(number) + " is a prime number"
            break

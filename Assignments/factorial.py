'''
program to find the factorial of a number.
'''
#reading a number to find factorial
number = int(input("Enter a number to find its factorial : "))
fact = 1
if number == 0 :
    print "factorial of number " + str(number) + " is 0"
for i in range(2,number+1):
    fact = fact * i
print "factorial of number " + str(number) + " is " + str(fact)
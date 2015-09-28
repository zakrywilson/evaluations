# Zach Wilson
# 09/27/2015

# Source Aaron Batilo 

for i in range(1, 101):
   if (i % 3) == 0 and (i % 5) == 0:
      print "FizzBuzz"
   elif (i % 3) == 0:
      print "Fizz"
   elif (i % 5) == 0:
      print "Buzz"
   else:
      print i

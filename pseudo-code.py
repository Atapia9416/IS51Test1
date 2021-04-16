"""
|======================|
|= Structured English =|
|======================|

The goal of the code is to compare two different salary options. Option 1 is a linearly increasing salary, you make $100
dollars per day consistently each day. Option 2 is an exponential function that starts you off with $1 dollar on the first day,
but you make twice as much the next day, so it is an exponential function. To determine which option will make you more money,
you first have to define option1 as its own variable and fine its value. It would be 10 days * $100. Then you would have to
calculate the value of option2 through an exponential function. Once both values have been determined you can create an if else 
statement. First you can use an if-elsif-else statement and test if both are equal, print "Option 1 and 2
pays the same," if Option 1 is greater print out "Option 1 is better" but if that is value, print out "Option 2 is better"
"""

"""
================
Pseudo Code
================

Set the value of option 1 by multiplying 10 * 100

set option2 to 0
Set a variable to count days to 0
Set pay variable to 1
set pay to 1

while day <= 10
add 1 to day
add pay to option2
multiply (pay * 2)

If Option1 is equal to option 2
    print Option1 and 2 are equal
elif Option 1 is greater
    print Option1 is better
else
    print option 2 is better

"""
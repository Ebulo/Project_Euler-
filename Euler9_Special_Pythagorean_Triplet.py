# Let Me Tell You How This is Done....
"""
So, satrt with,
a^2 + b^2 = c^2                         ----> eq1
a + b + c = 1000                        ----> eq2

from eq2, 
c = 1000 - a - b or c = 1000 - (a+b)    ----> eq3

put the eq3 in eq1,
a^2 + b^2 = (1000 - a - b)^2
after solving....
a = (1000^2 - 2000*b)/(2000 - 2*b)

Now we use b as a variable changing in a loop to find a
then, as we have b and a we find c from eq3
Now we only need to put the formula and find the values that's it....

"""


import math as m
for b in range(1, 1001):
    a = (1000**2 - 2000*b)/(2000 - 2*b)
    if m.floor(a) == a:                             # a is an integer
        c = (a*a + b*b)**.5
        print('a = ',a,'b = ', b, 'c = ', c)
        print("a*b*c = ", a*b*c)
        break
    else:                                           # a is not an integer
        pass

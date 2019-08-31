square = 0
sumSquare = 0
for i in range(101):
    square += i**2
    sumSquare += i

print("Square's_Sum is ", square, "\n", "Sum's_Ssquare is", sumSquare**2)
print("And Sum's_Square - Square's_Sum is", abs(sumSquare**2 - square))

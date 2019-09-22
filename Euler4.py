x = 0
y = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        a = i*j
        b = str(a)
        if b == b[::-1]:
            z = str(i) + '*' + str(j)
            x = b
            y = z

print("The greatest number is ", x, " Which is ", y)

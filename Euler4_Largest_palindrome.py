x = []
y = []
for i in range(100, 1000):
    for j in range(100, 1000):
        a = i*j
        b = str(a)
        if b == b[::-1]:
            z = str(i) + '*' + str(j)
            x.append(b)
            y.append(z)

print("The greatest number is ", x[-1], " Which is ", y[-1])

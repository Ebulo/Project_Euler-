x = []
n = int(input("Enter The Number"))
i = 2
while n > 1:
    while(n % i == 0):
        x.append(i)
        n /= i
    i += 1

print(x)
print("The greater Prime Factor is", x[-1], " And the smallest being", x[0])

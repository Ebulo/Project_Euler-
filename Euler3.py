x = 0
n = 600851475143
i = 2

while n > 1:
    while(n % i == 0):
        x = i
        n /= i
        
    i += 1

print("The greatest prime number is ","\"", x,"\"", " \n Happy Coding")

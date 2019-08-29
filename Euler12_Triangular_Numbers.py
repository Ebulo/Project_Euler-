
from math import sqrt

def count(n):
    d = {}
    c = 1

    while n % 2 == 0:
        n /= 2
        try:
            d[2] += 1
        except KeyError:
            d[2] = 1
    
    for i in range(3, int(sqrt(n+1)), 2):
        while n % i == 0 and i !=n:
            n = n / i
            try:
                d[i] += 1
            except KeyError:
                d[i] = 1

    d[n] = 1

    for _,v in d.items():
        c = c * (v + 1)
    return c


def tri_num(num):
    next = 1 + int(sqrt(1+(8*num)))
    return num + (next/2)


def main():
    i = 1
    while count(i) < 500:
        i = tri_num(i)
    return i


answer = main()
print("The Number is ", answer)

n = 400000

def fib(n):
    a = 0
    b = 1
    sm = 0
    for i in range(2, n):
        c = a + b
        a = b
        b = c
        if c >= n:
            break
        if c % 2 == 0:
            sm += c
    return sm
print(fib(n))

def mul():
    n = int(input("how many numbers"))
    sm = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            sm = sm + i
    return sm


print(mul()) # Should I write Comments That I wrote in my copy

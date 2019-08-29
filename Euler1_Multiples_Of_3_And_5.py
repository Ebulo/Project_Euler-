def mul():
    n = 1001
    sm = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            sm = sm + i
    return sm


print(mul())

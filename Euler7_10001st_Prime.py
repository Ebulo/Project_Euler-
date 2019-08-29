
def nextPrime(num):
    while True:
        num+=1
        for i in range(2, num):
            if num%i == 0:
                break
        else:
            return num
def getPrime(N):
    num, count = 1, 1
    while count<=N:
        num = nextPrime(num)
        yield num
        count += 1

N = 10001
l = [x for x in getPrime(N)]

print(l[-1]) # answer is 104743

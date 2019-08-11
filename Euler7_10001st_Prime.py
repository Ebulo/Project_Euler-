# solely taken help from youthoob, and did after understanding, I would try to develop my own way too...
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

N = 10001                                 # This might take a lot of time but you will get the answer which is 104743
l = [x for x in getPrime(N)]              # you can reduce the number and can check fast

print(l[-1]) # answer is 104743

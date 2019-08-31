pf = []
cf = []
def allPrimeFactors():
    for i in range(2, 21):
        primeFactors(i)
def primeFactors(n):
    k = n
    i = 2
    while k > 1:
        while (k%i == 0):
            pf.append(i)
            k /= i
        i += 1

allPrimeFactors()
print(pf)

count2 = 0
count3 = 0
count5 = 0
count7 = 0
count11 = 0
count13 = 0
count17 = 0
count19 = 0

for x in pf:
    if x == 2:
        count2 += 1

for x in pf:
    if x == 3:
        count3 += 1

for x in pf:
    if x == 5:
        count5 += 1

for x in pf:
    if x == 7:
        count7 += 1

for x in pf:
    if x == 11:
        count11 += 1

for x in pf:
    if x == 13:
        count13 += 1

for x in pf:
    if x == 17:
        count17 += 1

for x in pf:
    if x == 19:
        count19 += 1


count2 //= 4
cf.append(2**count2)
count3 //= 4
cf.append(3**count3)
count5 //= 4
cf.append(5**count5)
count7 //= 2
cf.append(7**count7)
cf.append(11**count11)
cf.append(13**count13)
cf.append(17**count17)
cf.append(19**count19)

ans = 1
for i in cf:
    ans *= i
print("The Smallest multiple is-", ans)

# Taken Help
import itertools
pbn = 2000000
numbers = list(range(3, pbn, 2))
pos = 0
while pos < len(numbers) - 1:
    number = numbers[pos]
    numbers = list(itertools.chain(itertools.islice(numbers, 0, pos + 1), itertools.filterfalse(lambda n: n % number != 0, itertools.islice(numbers, pos + 1, len(numbers)))))
    pos += 1

sop = sum(numbers) + 2
print(sop)

from sys import argv

n = None
if len(argv) > 1:
    n = int(argv[1])

def sieve(n):
    for i in range(n-1, 1, -1):
        print(n, i)
        if n % i == 0:
            return False
    return True

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]

for p in primes:
    print(sieve(p))

# given a num, check whether it is or isn't divisible by all that came before
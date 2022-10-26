def count_primes(n: int) -> int:
    if n <= 2: return 0
    primes = [True] * int(n+1)
    primes[0] = primes[1] = False
    for number in range(2,n+1):
        if primes[number]:
            for multiple in range(2*number,n+1,number):
                primes[multiple] = False
    return sum(primes)
t = int(input())
for i in range(t):
    l,r = map(int, input().split())
    k = 0
    for j in range(l,r+1):
        count = count_primes(j)
        if count % 2 == 0 and count >= 2:
            k += 1
    print(k)
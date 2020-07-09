def PrimeFactorization(x):
    'xを素因数分解する　返り値 type:dict key:prime value:exponent'
    prime = {}
    i = 2
    val = x
    while i*i <= x:
        if val%i == 0:
            prime[i] = 0
            while val%i == 0:
                val = val//i
                prime[i] += 1
        i += 1
    if val > 1:
        prime[val] = 1
    return prime

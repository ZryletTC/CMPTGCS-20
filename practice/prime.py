#is x prime?
def prime(x):
    for i in range (2,x):
        if x%i == 0:
            return False
    return True

#give all prime factors of x
def primeFactors(x):
    if prime(x):
        return [x]
    else:
        factors = []
        for i in range (2,x):
            multiple = True
            counter = 1
            while multiple:
                if (x%(i**counter) == 0) and prime(i):
                    factors.append(i)
                    counter = counter+1
                else:
                    multiple = False
        return factors

def nPrimes(n):
    counter = 0
    i = 2
    primelist = []
    while counter < n:
        if prime(i):
            counter = counter + 1
            primelist.append(i)
        i = i + 1
    return primelist

def nToNPrimes(n1,n2):
    primelist = []
    for i in range (n1,n2):
        if prime(i):
            primelist.append(i)
    return primelist

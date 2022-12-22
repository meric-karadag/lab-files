import math
def factorial(x):
    res = 1
    for i in range(1,x+1):
        res *= i
    return res
print(factorial(5))

def countdown(x):
    l = []
    for i in range(x,0,-1):
        l.append(i)
    return l

print(countdown(3))

def prime_factors(x):
    lst = []
    for i in range (1,x+1):
        if x % i == 0:
            if isprime(i):
                lst.append(i)
    return lst

def isprime(x):
    halfway = math.sqrt(x)
    if x == 0 or x == 1: return False
    if x == 2 or x == 3: return True
    for i in range(2,int(halfway)+2):
        if x % i == 0: return False
    return True

def proper_divisors(x):
    results = []
    for i in range(1,x):
        if x % i == 0:
            results.append(i)
    return results

def perfect_numbers(x):
    perf = []
    defic = []
    abund = []
    for i in range(1,x):
        if sum(proper_divisors(i)) == i:
            perf.append(i)
        elif sum(proper_divisors(i)) < i:
            defic.append(i)
        else:
            abund.append(i)
    result = (perf,defic,abund)
    return result

#print(perfect_numbers(8))

def pascal(x):
    results = [[] for i in range(x)]
    for i in range(x):
        for j in range(i+1):
    # nCr = n!/((n-r)!*r!)
            results[i].append(factorial(i)//(factorial(j)*factorial(i-j)))
    return results
#print(pascal(3))

def histogram(lst, bin):
    sorted(list(lst))
    results = [[]for i in range(bin)]
    for i in range(bin):
        for j in range(len(lst)//bin):
            results[i].append(lst[i*(len(lst)//bin)+j])
    return results

#print(histogram(range(100), 10))

def split(text, delimiters):
    results = []
    size = 0
    for i in range(len(text)):
        if text[i] in delimiters:
            results.append(text[i-size:i])
            size = 0
        size += 1
    return results
print(split('c,e,n,g,111,140', [',']))

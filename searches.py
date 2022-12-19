def bin_search(x,L):
    '''takes a list L in ascending order and returns whether x in L'''
    if len(L) == 0:
        return False
    mid_index = len(L)//2
    if x == L[mid_index]:
        return True
    elif x < L[mid_index]:
        return bin_search(x, L[:mid_index])
    elif x > L[mid_index]:
        return bin_search(x, L[mid_index+1:])

print(bin_search(4, [1,2,3,4,9,777,888,999]))


def head(L):
    return L[0]

def tail(L):
    return L[1:]

def insert(x,L):
    '''inserts x in the correct position in list L in an ascending order'''
    if len(L) == 0:
        return [x]
    if x < head(L):
        return [x] + L
    else:
        return [head(L)] + insert(x, tail(L))
    
def insertion_sort(L):
    if len(L) <=1:
        return L
    else:
        return insert(head(L), insertion_sort(tail(L)))

print(insertion_sort([5,2,4,6,1,3]))

def lcs(s1,s2):
    '''returns the lenght of the longest common sequence of s1 and s2'''
    if len(s1) == 0 or len(s2) == 0:
        return 0
    elif s1[-1] == s2[-1]:
        return 1 + lcs(s1[:-1], s2[:-1])
    else:
        return max(lcs(s1[:-1], s2), lcs(s1, s2[:-1]))

print(lcs('president', 'providence')) #expected outout = 6 priden


def fib (n) :
    '''calculating fibonacci series with making use of pre computed results'''
    results = [-1]* (n+1)
    results [0] = 0
    results [1] = 1
    return recursive_fib(results, n)
def recursive_fib (results, n) :
    if results [n] < 0:
        results[n] = recursive_fib(results, n-1)+recursive_fib(results,n-2)
    else:
        pass
        #print("using previous result") 
    return results[n]

print(fib(6))

def fib(n):
    '''accumulates values in the helper functions parameters'''
    if n == 0 or n == 1:
        return n 
    else:
        return fib_recursive(2, n, 1, 0)
def fib_recursive(i, n, fib_prev, fib_prev_prev):
    if i == n:
        return fib_prev + fib_prev_prev
    else:
        return fib_recursive(i+1, n, fib_prev+fib_prev_prev, fib_prev)

def seq_search(x,L):
    '''performs sequential search by for iteration'''
    for y in L:
        if x == y:
            return True
    return False

def seq_search2(x, L):
    '''performs sequential search with a while loop'''
    i = 0
    lenght = len(L)
    while i<lenght:
        if x == L[i]:
            return True
        i += 1
    return False

def bubble_sort(L):
    '''performs bubble sorting (sorting mechanism depends on consecutive comparisons)
    after one iteration ensures that the largest item is in the correct place'''
    length = len(L)
    changed = True
    while changed:
        changed = False
        i = 0
        while i < length-1:
            if L[i] > L[i+1]:
                (L[i], L[i+1]) = (L[i+1], L[i])
                changed = True
            i += 1
    return L

print(bubble_sort([5,2,4,6,1,3]))

#implementation of naive selection sort
def select_min(L):
    index = 0
    min = L[index]
    for i, x in enumerate(L):
        if x < min:
            index = i
            min = x
    L.pop(index)
    return min

def naive_selection_sort(L):
    '''performs selection sort, selects the smallest item at a time and place it and 
    adds it to an another list'''
    result = [0]*len(L)
    for i in range(0, len(L)):
        x = select_min(L)
        result[i] = x
    return result

def selection_sort(L):
    '''performs selection sort by finding the minumum of the reamaining sequence
    and swapping it with the first element of the remaining sequence'''
    lenght=len(L)
    i = 0
    while i < lenght-1:
        j = L.index(min(L[i:]))
        (L[i], L[j]) = (L[j], L[i])

def count_sort(L):
    '''performs counting sort on the List L presuming it ranges from 1,...k'''
    k = max(L)
    C = [0]*k
    #count the numbers in A
    for x in L:
        C[x-1] += 1
    
    result = []
    #extend the result list by the corresponding number i+1, x many times
    for i, x in enumerate(C):
        result.extend([i+1]*x)
    
    return result

print(count_sort([5,2,1,8,4,6,1,3,3]))

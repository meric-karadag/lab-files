import math

#print(countdown(3))

def the3N1P(x):
    if x == 1: return [1]
    elif x % 2 ==1: return [x] + the3N1P(3*x+1)
    elif x % 2 ==0: return [x] + the3N1P(x/2)
def the3N1P1(x):
    list1 = []
    while x != 1:
        list1.append(x)
        if x % 2 ==1: x = 3*x+1
        elif x % 2 == 0: x = x/2
    return list1 + [1]
#print(the3N1P(22)) 
#print(len(the3N1P1(9)))

def max3n1p(x):
    max = 1
    cache = 1
    for i in range(2,x+1):
        if len(the3N1P1(i)) > max:
            max = len(the3N1P1(i))
            cache = i
    return cache, max

#print(max3n1p(500))

def isprime(x):
    halfway = math.sqrt(x)
    if x == 0 or x == 1: return False
    if x == 2 or x == 3: return True
    for i in range(2,int(halfway)+2):
        if x % i == 0: return False
    return True

"""print(isprime(2))
print(isprime(3))
print(isprime(4))
print(isprime(5))"""

def triangle(x):
    for i in range(1,x+1):
        str = " "*(x-i)+"*"*(2*i-1)
        print(str)

#print(triangle(7))

def lis(x):
    longest = 1
    alternative = 1
    lenght = len(x)
    for i in range(1,lenght):
        if x[i] >= x[i-1]:
            alternative += 1
        else:
            alternative = 1
        if alternative > longest:
            longest = alternative
    return longest

"""print(lis([1, 2, 3, 4, 3, 5, 6]))
print(lis([1, 1, 2, 3, 4, 5, 1]))
print(lis([3, 2, 1]))"""

def matrix_mul(X,Y):
    result = [[[0]*len(Y[0])] for i in range(len(X))]
    for i in range(len(X)):
    # iterate through columns of Y
        for j in range(len(Y[0])):
       # iterate through rows of Y
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]



    return result
#print( matrix_mul( [[1,2,3], [4,5,6], [7,8,9]], [[7,8,9], [4,5,6], [1,2,3]] ))

#print([[[0]*4] for i in range(5)])

def prime_factors(x):
    lst = []
    for i in range (1,x+1):
        if x % i == 0:
            if isprime(i):
                lst.append(i)
    return lst

#print(prime_factors(66))

def ispal(y):
        return True if str(y) == (str(y))[::-1] else False
def palindromes(x):
    result = []
    
    for i in range(x):
        if ispal(i) and ispal(bin(i)[2:]):
            result.append(i)
    return result

#print(palindromes(1000))

def triplets(x):
    result = []
    for i in range(1,x):
        for j in range(i,x):
            for k in range(j,x):
                if i**2 + j**2 == k**2:
                    result.append((i,j,k))
    return result
#print(triplets(20))

def fibseries(x):
    if x == 1:
        return 0
    elif x == 2:
        return [0,1]
    elif x > 2:
        return fibseries(x-1) + [fibseries(x-1)[-1] + fibseries(x-1)[-2]]

#print(fibseries(10))

def myrange(start,stop,step):
    if stop <= start:
        return []
    else:
        return [start] + myrange(start+step,stop,step)
#print(myrange(3,15,3))

def count_item(obj,lst):
    if len(lst) == 0:
        return 0
    elif obj == lst[0]:
        return 1 + count_item(obj,lst[1:])
    else:
        return 0 + count_item(obj, lst[1:])
#print(count_item(1, [1,2,3,1,1,3,1]))

def keep_numbers(x):
    if len(x) == 0: return []
    
    if type(x[0]) == float or type(x[0]) == int:
            return [x[0]] + keep_numbers(x[1:])
    else:
        return keep_numbers(x[1:])

#print(keep_numbers([1, 2, '45', 'ceng', 3.4]))

def keep(func, lst):
    if len(lst) ==0:
        return []
    if func(lst[0]):
        return [lst[0]] + keep(func, lst[1:])
    else:
        return keep(func, lst[1:])

#print(keep(str.islower, ['Abc', 'abc', 'CENG', '45', 'ceng', '111']))

def every(func , lst):
    if len(lst) ==0:
        return []

    return [func(lst[0])] + every(func, lst[1:])

#print(every(str.upper, ['ceng', '111', 'ceng111', 'abcdefgh']))

def remove_item(obj,lst):
    if len(lst) == 0:
        return []
    if lst[0] == obj:
        return remove_item(obj,lst[1:])
    else:
        return [lst[0]] + remove_item(obj, lst[1:])

#print(remove_item('ceng', [1,2,3,4,'ceng',5,6,7]))

def letter_pairs(x):
    if len(x) < 2:
        return []
    return [x[0]+x[1]] + letter_pairs(x[1:])

#print(letter_pairs('tripoli'))

def progressive_square(lst):
    if len(lst) == 1: return True
    return progressive_square(lst[1:]) if lst[0] **2 == lst[1] else False

#print(progressive_square([2,4,16,256]))
#print(progressive_square([1,2,3,7]))

def sum_numbers(lst):
    if len(lst) == 0:
        return 0
    if type(lst[0]) == int or type(lst[0]) == float:
        return lst[0] + sum_numbers(lst[1:])
    else:
        return 0 + sum_numbers(lst[1:])

#print(sum_numbers([1,3,4,5,'gse',[12,43,5],'14']))

def is_substring(sbs,str):
    if len(sbs)>len(str):
        return False
    if sbs == str[:len(sbs)]:
        return True
    else:
        return is_substring(sbs, str[1:])
    
#print(is_substring('ssip', 'mississippi'))
#print(is_substring('misip', 'mississippi'))

def substrings(x):
    if len(x) ==0 : return []
    if len(x) == 1 : return [x]
    return [x[0] + x[1:i] for i in range(1,len(x)+1)] + substrings(x[1:])

#print(substrings('ceng'))

def branch(indices, lst):
    if len(indices) == 1:
        return lst[indices[0]]
    else:
        return branch(indices[1:], lst[indices[0]])

#print(branch([2], [['a', 'b'], ['c', 'd'], ['e', 'f'], ['g', 'h']]) )
#print(branch([1, 2, 0, 1], [['a', 'b'], [['c', 'd'], ['e', 'f'], [['g', 'h'], ['i', 'j']], 'k'], ['l', 'm']]))

def flatten(lst):
    if len(lst) ==0:
        return []
    if type(lst[0]) != list:
        return [lst[0]] + flatten(lst[1:])
    else:
        return(flatten(lst[0])) + flatten(lst[1:])

#print(flatten([1,[2],3,4]))
#print(flatten([1,[[2],3],4]))
#print(flatten([1,[[2],3],[[[4]]]]))

def sum_all(lst):
    if len(lst) == 0:
        return 0
    if type(lst[0]) != list:
        return lst[0] + sum_all(lst[1:])
    else:
        return sum_all(lst[0]) + sum_all(lst[1:])

#print(sum_all([[1, 2, [3]], [4, 5], [6, 7]]))

def reverse_lists(lst):
    if len(lst) ==0:
        return []
    if type(lst[-1]) != list:
        return [lst[-1]] + reverse_lists(lst[:-1])
    else:
        return [reverse_lists(lst[-1])] + reverse_lists(lst[:-1])

#print(reverse_lists([1, 2, [3, 4], 5, [6, [7, [8, 9], 10], 11], 12]))

'''def search_file(file, directory):
    if len(directory) ==0:
        return ''
    if type(directory[0])==str:
        return directory[0] + search_file(file,directory[1:])
    else:
        if file in directory:
            return directory[0] + '/' + file
        else:
            return search_file(file, directory[1:])'''

#print(search_file('hw1.pdf', ['Documents', ['abc'], ['ceng111', 'hw1.pdf'], 'deneme.py', 'chapter3.pdf']))

def palindrome(s):
    if len(s) <=1:
        return True
    else:
        return s[0] == s[-1] and palindrome(s[1:-1])

#print(palindrome('moom'))


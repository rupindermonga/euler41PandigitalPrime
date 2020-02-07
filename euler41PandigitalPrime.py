'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''

def IsPandigital(list_new):
    result = False
    set_new = set(list_new)
    if len(list_new) == len(set_new) and set_new == set(range(1, len(list_new)+1)) :
        result = True
    return result

def isPrime(n):
    result = True
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            result = False
            break
    return result

def PandigitalPrime():
    result = 0
    for i in range(7654321,1,-2): # sum of all digits divided by 3 is divisible by 3 so there is no prime above 7 digits
        new_str = list(str(i))
        for j in range(0, len(new_str)): 
            new_str[j] = int(new_str[j]) 
        #if '0' not in new_str and len(set(new_str)) == len(new_str):
        if IsPandigital(new_str):
            if isPrime(i):
                result = i
                break
    return result

final = PandigitalPrime()
print(final)
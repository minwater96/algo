import math

def solution(numer1, denom1, numer2, denom2):

    numer = (numer1 * denom2) + (numer2 * denom1)
    denom = (denom1 * denom2)
    
    g = math.gcd(denom, numer)
   
    return [numer//g, denom//g]


print(solution(1, 2, 3, 4)) # => [5, 4]
print(solution(9, 2, 1, 3)) # => [29, 6]
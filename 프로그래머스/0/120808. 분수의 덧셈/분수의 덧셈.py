import math

def solution(numer1, denom1, numer2, denom2):
    numer = 0
    answer = []
    gcd = 0
    if denom1 != denom2:
        numer1 *= denom2
        numer2 *= denom1
        denom1 *= denom2
        denom2 = denom1
        numer = numer1 + numer2
    if denom1 == denom2:
        numer = numer1 + numer2
    gcd = math.gcd(numer, denom1)
    
    numer /= gcd
    denom1 /= gcd
    
    answer.append(numer)
    answer.append(denom1)
    
    return answer
import math

def solution(a, b):
    
    gcd = math.gcd(a, b)
    
    b = b // gcd
    
    if b % 2 == 0:
        while b % 2 == 0:
            b = b // 2
    
    if b % 5 == 0:
        while b % 5 == 0:
            b = b // 5
        
    if b == 1:
        return 1

    return 2
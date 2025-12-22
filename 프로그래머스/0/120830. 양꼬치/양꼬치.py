def solution(n, k):
    
    s = n * 12000
    d = 2000 * k
    total = s + d
    
    sale = (n // 10) * 2000
    
    
    
    if (n // 10) >= k:
        total -= d
    else:
        total -= sale
    
    return total
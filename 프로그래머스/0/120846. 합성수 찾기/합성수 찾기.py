def solution(n):
    
    s = 0
    
    for i in range(1, n+1):
        tmp = 0
        for j in range(1, n+1):
            if i % j == 0:
                tmp += 1
        if tmp >= 3:
            s += 1
            
    return s
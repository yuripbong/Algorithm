def solution(slice, n):
    i = 1
    while(1):
        if (slice * i) >= n:
            break
        i += 1
    
    return i
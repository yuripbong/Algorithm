def solution(n):
    answer = []
    result = []
    
    for i in range(2, n+1):
        is_prime = True
        
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime == True:
            answer.append(i)
            
    for i in answer:
        if n % i == 0:
            result.append(i)
    
    return result
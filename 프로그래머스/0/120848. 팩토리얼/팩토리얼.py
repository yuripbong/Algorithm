def solution(n):
    answer = 0
    
    def factorial(x):
        if (x > 1):
            return x * factorial(x - 1)
        else:
            return 1
    
    for i in range(1, 12):
        if n < factorial(i):
            answer = i - 1
            break
        
    return answer
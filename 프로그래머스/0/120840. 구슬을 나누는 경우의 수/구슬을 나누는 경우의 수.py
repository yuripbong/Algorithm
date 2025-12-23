def solution(balls, share):
    answer = 0
    
    def factorial(n):
        if (n > 1):
            return n * factorial(n - 1)
        else:
            return 1
        
    balls_f = factorial(balls)
    share_f = factorial(share)
    bms_f = factorial(balls-share)
    
    answer = balls_f/(bms_f * share_f)
    
    return answer
def solution(chicken):
    
    answer = 0
    coupon = chicken
    
    while coupon >= 10:
        service = coupon // 10
        left_coupon = coupon % 10
        
        answer += service
        
        coupon = service + left_coupon
        
    return answer
        
        
        
        
    
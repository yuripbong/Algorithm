def solution(numbers):
    answer = 0
    
    numbers = sorted(numbers)
    
    min1 = numbers[0]
    min2 = numbers[1]
    max1 = numbers[-1]
    max2 = numbers[-2]
    
    if min1 * min2 > max1 * max2:
        answer = min1 * min2
    else:
        answer = max1 * max2
    
    
    return answer
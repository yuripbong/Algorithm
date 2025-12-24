def solution(numbers, k):
    
    i = k - 1
    
    r = (i * 2) % len(numbers)
    
    return numbers[r]
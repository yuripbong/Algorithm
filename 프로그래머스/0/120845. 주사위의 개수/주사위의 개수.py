def solution(box, n):
    
    s = box[0] // n
    g = box[1] // n
    n = box[2] // n
    
    return s * g * n
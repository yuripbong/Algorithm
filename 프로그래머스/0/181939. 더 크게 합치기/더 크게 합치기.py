def solution(a, b):
    answer = 0
    a = str(a)
    b = str(b)
    case1 = int(a + b)
    case2 = int(b + a)
    
    if case1 >= case2:
        answer = case1
    else:
        answer = case2
    return answer
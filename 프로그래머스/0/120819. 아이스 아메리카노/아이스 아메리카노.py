def solution(money):
    answer = []
    
    jan = money // 5500
    rest = money % 5500
    
    answer.append(jan)
    answer.append(rest)
    
    return answer
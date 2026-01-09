def solution(sides):
    answer = 0
    
    # 가장 긴 변이 sides에 있는 경우 
    for i in range(max(sides) - min(sides), max(sides)):
        answer += 1
        
    print(answer)
        
    x = max(sides) + 1
    # 나머지 한 변이 가장 긴 변인 경우
    while (sides[0] + sides[1]) > x:
        answer += 1
        x += 1
    return answer
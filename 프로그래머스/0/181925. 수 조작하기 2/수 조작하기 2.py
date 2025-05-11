def solution(numLog):
    answer = ''
    for i in range(len(numLog) - 1):
        sub = numLog[i+1] - numLog[i]
        if sub == 1:
            answer += "w"
        elif sub == -1:
            answer += "s"
        elif sub == 10:
            answer += "d"
        elif sub == -10:
            answer += "a"
        
    return answer
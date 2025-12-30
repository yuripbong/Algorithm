def solution(s):
    answer = []
    s = s.split(" ")
    print(s)
    
    for i in range(len(s)):
        answer.append(s[i])
        if s[i] == 'Z':
            answer.pop()
            answer.pop()
            
    print(s)
    print(answer)
    
    for i in range(len(answer)):
        answer[i] = int(answer[i])
    
    return sum(answer)
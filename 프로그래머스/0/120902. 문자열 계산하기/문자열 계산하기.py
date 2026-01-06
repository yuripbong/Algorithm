def solution(my_string):
    s = my_string.split(' ')
    h = 0
    f = 0
    t = 0
    
    answer = int(s[0])
        
    for i in range(1, len(s), 2):
        op = s[i]
        num = int(s[i+1])
        
        if op == '+':
            answer += num
        if op == '-':
            answer -= num
            
    return answer
        

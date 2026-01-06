def solution(quiz):
    answer = []
    
    for i in range(len(quiz)):
        tmp = quiz[i].split(' ')
        print(tmp)
        x = int(tmp[0])
        op = tmp[1]
        y = int(tmp[2])
        res = int(tmp[4])
        
        
        if op == '+':
            sol = x + y
        else:
            sol = x - y
            
        if sol == res:
            answer.append('O')
        else:
            answer.append('X')
    
    return answer
def solution(spell, dic):
    answer = 2
    
    for i in range(len(dic)):
        tmp = 0
        for j in range(len(spell)):
            if spell[j] in dic[i]:
                tmp += 1
            else:
                break
        if tmp == len(spell):
            answer = 1
        
    return answer
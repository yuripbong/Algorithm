def solution(emergency):
    
    em_len = len(emergency)
    answer = [em_len] * em_len
    
    for i in range(em_len):
        for j in range(em_len):
            if emergency[i] > emergency[j]:
                answer[i] -= 1
    
    return answer
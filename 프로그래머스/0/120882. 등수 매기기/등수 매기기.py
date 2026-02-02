def solution(score):
    answer = [1] * len(score)
    avg = []
    
    for i in range(len(score)):
        avg.append(sum(score[i]))
        
    print(avg)
    
    for i in range(len(avg)):
        for j in range(i+1, len(avg)):
            if avg[i] > avg[j]:
                answer[j] += 1
            elif avg[i] < avg[j]:
                answer[i] += 1
        
    return answer
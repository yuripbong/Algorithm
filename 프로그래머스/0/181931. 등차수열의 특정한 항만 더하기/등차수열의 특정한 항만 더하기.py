def solution(a, d, included):
    answer = 0
    arr = []
    
    for i in range(len(included)):
        arr.append(a + d*i)
        
    for i in range(len(included)):
        if included[i] == True:
            answer += arr[i]
        
    return answer
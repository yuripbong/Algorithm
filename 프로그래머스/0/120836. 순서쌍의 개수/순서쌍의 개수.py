def solution(n):
    answer = 0
    
    n_list = []
    for i in range(1, n+1):
        if n % i == 0:
            n_list.append(i)
            
    for i in n_list:
        for j in range(len(n_list)):
            if i * n_list[j] == n:
                answer += 1
        
    return answer
def solution(clothes):
    
    answer = 0
    clothes_len = len(clothes) # 의상 개수
    clothes_arr = [] # 의상 이름
    kind_arr = [] # 의상 종류
    
    # answer += clothes_len
    
    for i in range(clothes_len):
        for j in clothes:
            if j[1] not in kind_arr:
                kind_arr.append(j[1])
    
    dic = {}
    for i in kind_arr:
        dic[i] = 1
    
    for i in range(clothes_len):
        dic[clothes[i][1]] += 1
        
    kind_num = list(dic.values())
    
    tmp = 1
    for i in range(len(kind_num)):
        tmp *= kind_num[i]
        
    answer = tmp -1
    
    return answer
    
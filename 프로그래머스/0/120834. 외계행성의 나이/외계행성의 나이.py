def solution(age):
    
    age_list = list(str(age))
    s_list = []
    
    for i in range(len(age_list)):
        s_list.append(chr(int(age_list[i])+97))
        
    return ''.join(s_list)
    
    
    
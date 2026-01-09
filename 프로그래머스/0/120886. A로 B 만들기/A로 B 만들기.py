def solution(before, after):
    answer = 0
    
    before_list = sorted(list(before))
    after_list = sorted(list(after))
    
    print(before_list)
    print(after_list)
    
    if before_list == after_list:
        answer = 1
        
    return answer
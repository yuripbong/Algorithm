def solution(my_string):
    answer = 0
    
    for i in range(len(my_string)):
        if my_string[i].isdigit() == False:
            my_string = my_string.replace(my_string[i], ' ')
            
    print(my_string)
    
    num_list = my_string.split()
    
    for i in num_list:
        answer += int(i)
    
    return answer
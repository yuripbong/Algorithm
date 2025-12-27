def solution(my_string):
    answer = []
    
    if 'a' or 'e' or 'i' or 'o' or 'u' in my_string:
        for i in range(len(my_string)):
            if my_string[i] == 'a' or my_string[i] == 'e' or my_string[i] == 'i' or my_string[i] == 'o' or my_string[i] == 'u':
                pass
            else:
                answer.append(my_string[i])
    
    return ''.join(answer)
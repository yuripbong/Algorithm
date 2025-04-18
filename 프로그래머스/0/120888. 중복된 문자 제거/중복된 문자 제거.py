def solution(my_string):
    my_string = list(my_string)
    answer = {}
    for i in range(len(my_string)):
        if my_string[i] not in answer:
            answer[my_string[i]] = i
    an = ''
    for key in answer:
        an += key
    return an

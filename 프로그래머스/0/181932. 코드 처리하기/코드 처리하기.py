def solution(code):
    mode = 1
    answer = ''
    for i in range(len(code)):
        if code[i] == "1":
            mode = 1 - mode
            continue
            
        if mode == 1 and i % 2 == 0:
            answer += code[i]
        elif mode == 0 and i % 2 == 1:
            answer += code[i]
    if answer == "":
        answer = "EMPTY"
    return answer
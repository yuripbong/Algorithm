def solution(keyinput, board):
    answer = [0, 0]
    
    for i in keyinput:
        
        if i == "left":
            if answer[0] > -(board[0] // 2):
                answer[0] -= 1
            else:
                continue
        elif i == "right":
            if answer[0] < (board[0] // 2):
                answer[0] += 1
            else:
                continue
        elif i == "up":
            if answer[1] < (board[1] // 2):
                answer[1] += 1
            else:
                continue
        else:
            if answer[1] > -(board[1] // 2):
                answer[1] -= 1
    return answer
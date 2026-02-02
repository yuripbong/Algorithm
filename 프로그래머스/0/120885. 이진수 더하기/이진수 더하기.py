def solution(bin1, bin2):
    answer = []
    carry = 0
    
    # bin1, bin2 길이 맞추기
    if len(bin1) > len(bin2):
        bin2 = bin2.zfill(len(bin1))
        
    if len(bin1) < len(bin2):
        bin1 = bin1.zfill(len(bin2))
        
    
    for i in range(len(bin1)-1, -1, -1):
        tmp = carry + int(bin1[i]) + int(bin2[i])
        
        if tmp == 2:
            answer.append('0')
            carry = 1
        elif tmp == 3:
            answer.append('1')
            carry = 1
        elif tmp == 1:
            answer.append('1')
            carry = 0
        elif tmp == 0:
            answer.append('0')
            carry = 0
    
    # 마지막 carry 더함
    if carry == 1:
        answer.append('1')
        
    answer = answer[::-1]
    answer = ''.join(answer)
    
    
    return answer
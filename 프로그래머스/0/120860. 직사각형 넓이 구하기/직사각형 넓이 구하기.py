def solution(dots):
    
    max_width = dots[0][0]
    min_width = dots[0][0]
    max_height = dots[0][1]
    min_height = dots[0][1]
    
    for i in range(len(dots)):
        if max_width < dots[i][0]:
            max_width = dots[i][0]
        if min_width > dots[i][0]:
            min_width = dots[i][0]
        if max_height < dots[i][1]:
            max_height = dots[i][1]
        if min_height > dots[i][1]:
            min_height = dots[i][1]
    
    return (max_width - min_width) * (max_height - min_height)
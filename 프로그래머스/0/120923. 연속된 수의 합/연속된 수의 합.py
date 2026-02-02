def solution(num, total):
    # 1. 시작 숫자 구하기 (수학 공식)
    # 평균(total // num)에서 절반 거리((num - 1) // 2)만큼 뺀 위치가 시작점
    start = (total // num) - ((num - 1) // 2)
    
    # 2. 시작 숫자부터 num개만큼 리스트 만들기
    # 예: start가 3이고 num이 3이면 -> range(3, 6) -> [3, 4, 5]
    return list(range(start, start + num))
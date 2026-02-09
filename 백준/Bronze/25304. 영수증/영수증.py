x = int(input()) # 총 금액
n = int(input()) # 구매한 물건의 종류의 수

sum = 0
# 각 물건의 가격, 개수
for i in range(n):
    a, b = map(int, input().split())
    sum += a*b
    
if sum == x:
    print("Yes")
else:
    print("No")

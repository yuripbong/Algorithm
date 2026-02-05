# n: 바구니 개수
# m: 공 교환 횟수
n, m = map(int, input().split())

n_list = [0]

for i in range(1, n+1):
    n_list.append(i)
    
for i in range(m):
    x, y = map(int, input().split())
    
    n_list[x], n_list[y] = n_list[y], n_list[x]
    
    
print(*n_list[1:])

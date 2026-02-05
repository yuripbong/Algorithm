n, m = map(int, input().split())
n_list = [0] * n

for ball in range(m):
    i, j, k = map(int, input().split())
    
    for basket in range(i-1, j):
        n_list[basket] = k
        
print(*n_list)

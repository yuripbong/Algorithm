arr = list(map(int, input().split()))

for i in range(3):
    if arr.count(arr[i]) == 2:
        print(1000 + (arr[i]*100))
        exit()
    if arr.count(arr[i]) == 3:
        print(10000 + (arr[i]*1000))
        exit()

print(max(arr)*100)

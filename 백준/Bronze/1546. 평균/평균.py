n = int(input())

grade = list(map(int, input().split()))

grade_max = max(grade)
max_index = grade.index(grade_max)

new_grade = []
for i in range(n):
    new_grade.append(grade[i]/grade_max*100)
    
print(sum(new_grade)/n)

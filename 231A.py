n1 = 3
prob1 = [1, 1, 0]
prob2 = [1, 1, 1]
prob3 = [1, 0, 0]

problems = [prob1, prob2, prob3]
result = 0

for i in range(n1):
    count = 0
    for j in range(3):
        if problems[i][j] == 1:
            count += 1
    if count >= 2:
        result += 1

print(result)

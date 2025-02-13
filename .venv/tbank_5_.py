num_from, num_to = map(int, input().split())
res = []
result = []

for i in range(len(str(num_to))):
    for j in range(1, 10):
        res.append(j * int('1' * (i + 1)))

#print(res)

for i in range(len(res)):
    if num_from <= res[i] <= num_to:
        result.append(res[i])

#print(result)
print(len(result))
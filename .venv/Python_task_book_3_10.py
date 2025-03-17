number = 10
my_list = [10, 2, 3000, 404, 30405, 607, 808080, 909099]
res = []

for i in range(len(my_list)):
    if number % my_list[i] == 0:
        res.append(my_list[i])

print(res)

res = []
for i in range(len(my_list)):
    if len(str(my_list[i])) == 1:
        res.append(my_list[i])

print(res)

res = []
num1 = 123457
num2 = 45362765

set1 = [int(symbol) for symbol in str(num1)]
set2 = [int(symbol) for symbol in str(num2)]

res = set(set1)&set(set2)
print (res)


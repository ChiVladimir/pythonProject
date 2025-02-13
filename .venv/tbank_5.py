from math import floor, log10

num_from, num_to = map(int, input().split())

list_res = []
res = 0

for n in range(num_from, num_to + 1):
#    print(n, set(list(str(n))))
    if len(set(list(str(n)))) == 1:
        list_res.append(n)

print(len(list_res))
print(list_res)
print("========")

res = 0
num_dgt_from = floor(log10(num_from)) + 1
num_dgt_to   = floor(log10(num_to)) + 1
print ("1 - ", num_dgt_from, num_dgt_to)

res = 9 * (num_dgt_to - num_dgt_from + 1)
minus_from = 0
minus_to = 0

#count_before = int(str(num_from)[0])
count_before = 0
for i in range(num_dgt_from):
    count_before += int(str(num_from)[0]) * (10 ** i)
print ("2 - ", count_before, num_from)

if count_before < num_from:
    minus_from = (int(str(num_from)[0]))# + 9 * (num_dgt_from - 1)
else:
    minus_from = (int(str(num_from)[0]) - 1)# + 9 * (num_dgt_from - 1)

#count_after = int(str(num_to)[0])
count_after = 0
for i in range(num_dgt_to):
    print(i, int(str(num_to)[0]) * (10 ** i))
    count_after += int(str(num_to)[0]) * (10 ** i)
print ("3 - ", count_after, num_to)

if count_after > num_to:
    minus_to = (10 - int(str(num_to)[0]))
else:
    minus_to = (9 - int(str(num_to)[0]))


print("4 - ", minus_from, minus_to)
print(res, (res - minus_from - minus_to))


l, r = map(int, input().split())

num_from, num_to = map(int, input().split())
res = set()
result = 0

for i in range(len(str(num_to))):
    for j in range(1, 10):
        res.add(j * int('1' * (i + 1)))
result = len([x for x in res if x >= num_to and x <= num_to])
print(result)
from math import floor, log10

num_from, num_to = map(int, input().split())

res = 0

if num_from > num_to:
    print (0)
    exit()

num_dgt_from = floor(log10(num_from)) + 1
num_dgt_to   = floor(log10(num_to)) + 1

res = 9 * (num_dgt_to - num_dgt_from + 1)
minus_from = 0
minus_to = 0

count_before = 0
for i in range(num_dgt_from):
    count_before += int(str(num_from)[0]) * (10 ** i)

if count_before < num_from:
    minus_from = (int(str(num_from)[0]))# + 9 * (num_dgt_from - 1)
else:
    minus_from = (int(str(num_from)[0]) - 1)# + 9 * (num_dgt_from - 1)

count_after = 0
for i in range(num_dgt_to):
    count_after += int(str(num_to)[0]) * (10 ** i)

if count_after > num_to:
    minus_to = (10 - int(str(num_to)[0]))
else:
    minus_to = (9 - int(str(num_to)[0]))

print(res - minus_from - minus_to)



qnt_of_stds = int(input())
rank = [int(n) for n in input().split()]

pairs = {}

list_odd = []
list_even = []

x = y = -1

for pos, rost in enumerate(rank, start=1):
    if pos%2 != rost%2:
        if rost % 2 == 0:
            list_odd.append(pos)
        elif rost % 2 != 0:
            list_even.append(pos)
if len(list_odd) == 1 and len(list_even) == 1:
    x = list_odd[0]
    y = list_even[0]

elif len(list_odd) == 0 and 0 == len(list_even):
    if qnt_of_stds >= 3:
        x, y = 1, 3
print(x, y)
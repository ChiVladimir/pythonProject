my_str = 'abcde abcde abcde'

res_str = my_str.split(' ')
for i in range(len(res_str)):
    res_str[i] = f"{res_str[i][:-1]}{res_str[i][-1].upper()}"

print(" ".join(res_str))

txt1 = '12345'
txt2 = '45678'

print(list(txt1))
overlap = set(list(txt1)) & set(list(txt2))
print("".join(sorted(overlap)))

my_str = 'a bc def ghij'
res = []

for i in range(len(my_str.split(' '))):
    if len(my_str.split(' ')[i]) <= 3:
        res.append(my_str.split(' ')[i].upper())
    else: res.append(my_str.split(' ')[i])
print(" ".join(res))

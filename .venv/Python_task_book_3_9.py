from http.cookiejar import uppercase_escaped_char

my_list = [10, 3000, 404, 30405, 607, 808080, 909099]
res = []
n = 0
for i in range(len(my_list)):
    n = 0
    for j in range(len(str(my_list[i]))):
        if "0" in ((str(my_list[i])[j])):
            n += 1
    if n < 2:
        res.append(my_list[i])

print(res)

res = []
i = 1
while i <= 1000:
    sum = 0
    for j in range(len(str(i))):
        sum += int(str(i)[j])
    if sum == 13:
        res.append(i)
    i += 1
print (res)

my_list = [1, 2, 3]
print (sorted(my_list + my_list))

lst1 = [1, 2, 3]
lst2 = [4, 5, 6]

for i in range(len(lst1)):
    print (f"'{lst1[i]},{lst2[i]}'")
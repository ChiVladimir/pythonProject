from http.cookiejar import uppercase_escaped_char

my_list = [1, 3, 44, 345, 67, 888, 9999]
res = []
n = 0
for i in range(len(my_list)):
    if "3" in str(my_list[i]):
        n += 1

if n == (len(my_list)):
    print ("all elements include 3")
else:
    print("not all elements include 3")

my_str = "1, 3, 44, 345, 67, 888, 9999"

print((sorted((my_str.split(", ")), reverse=True))[0])



my_str = 'kebab-case'

res_str = my_str.split('-')

print("_".join(res_str))



my_str = 'camelCaseCaseCaseCase'
my_list = []
for i in range(len(my_str)):
    if my_str[i].isupper():
        my_list.append("_" + my_str[i].lower())
    else:
        my_list.append(my_str[i])

print("".join(my_list))
my_num = 1357
for i in range(len(str(my_num))):
    if int(str(my_num)[i]) % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

my_str = 'abcba'
my_str_rev = my_str[::-1]

if my_str_rev == my_str:
    print("Equal")
else: print("Not equal")

st1 = {1, 2, 3}
st2 = {4, 5, 6}

st3 = st1 | st2
print (st3)

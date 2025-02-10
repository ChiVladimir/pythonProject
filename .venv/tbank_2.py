count_of_people= int(input())


print((count_of_people - 1).bit_length())
print(count_of_people.bit_length() - (count_of_people & (count_of_people - 1) == 0))


count_of_cuts = 0
p = 1
while p < count_of_people:
    count_of_cuts += 1
    p *= 2
print(count_of_cuts)
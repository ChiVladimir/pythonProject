def is_vowel(check_letter):
    all_vowels = 'aeiouаоэеиыуёюя '
    return check_letter in all_vowels


my_str = "Каждая буква величиною в метр и нарисована масляной краской!Each letter is three feet high, and they used oil paints."

my_str_without_vowels = []

for i in range(len(my_str)):
    if is_vowel(my_str[i]) is False:
        my_str_without_vowels.append(my_str[i])
    else: continue

print("".join(my_str_without_vowels))

st1 = {1, 2, 3, 4, 5}
st2 = {4, 5, 6, 7, 8}

overlap = set(st1) & set(st2)
print(overlap)

all_without_overlap = st1 ^ st2

print(all_without_overlap)

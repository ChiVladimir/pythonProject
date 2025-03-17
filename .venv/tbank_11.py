import time

def inverse_num_mod(a, p): # Функция для определения обратного по модулю p, по тз - малая теорема Ферма: a^(p-2) % p
    return power(a, p - 2, p)

def power(base, exp, mod): # Функция возведения в степень: (base^exp) % mod
    res = 1

    while exp > 0:
        if exp % 2 == 1:
            res = (res * base) % mod
        base = (base * base) % mod
        exp //= 2
    return res

input_data = [int(n) for n in input().split()]

start_time = time.time()

l = int(input_data[0])
r = int(input_data[1])
p = int(input_data[2])

if p < 2 or p <= r or l < 1 or r < 1 or l > r:
    print(0)
    exit()
f = [0] * (r - l + 1)  # массив для "префиксов"

# Вычисляем произведения префиксов: f(k) = f(k-1) * k % p
for k in range(len(f)):
    if k == 0:
        f[0] = l % p
    else:
        f[k] = (f[k - 1] * (l + k)) % p

# Определяем обратное по модулю p для последнего префикса
inverse_num = inverse_num_mod(f[-1], p)
sum_result = 0

# Считаем обратные числа F(k) = f(k)^-1 * f(k-1)% p
for k in range(r - l, 0, -1):
    sum_result += (inverse_num * f[k - 1]) % p
    inverse_num = (inverse_num * (k + l)) % p
sum_result += inverse_num

print(sum_result % p)  # результат - сумма обратных чисел по модулю p

finish_time = time.time()
print(f'Time: {(finish_time-start_time)} seconds')
from collections import deque

N = int(input()) - 1
coins = list(map(int, input().split()))

mod = max(coins) if coins else 0
full_cycles = N // mod  # Считаем общее число циклов
full_rest = N % mod  # Определяем итоговые остатки

# Массив для хранения минимального количества циклов для каждого остатка
reachable_rests = [-1] * mod
reachable_rests[0] = 1  # Остаток 0 достижим сразу

# Очередь для хранения текущих достижимых остатков и количества циклов до них
queue = deque([(0, 1)])  # Пара: (остаток, количество циклов)

# Пока есть остатки для проверки
while queue:
    rest, cycles = queue.popleft()

    # Проверяем все монеты
    for coin in coins:
        # Вычисляем новый остаток
        new_rest = (rest + coin) % mod
        new_cycles = cycles + (rest + coin) // mod

        # Если остаток ещё не был достигнут или достигнут с меньшим числом циклов
        if reachable_rests[new_rest] == -1 or reachable_rests[new_rest] > new_cycles:
            reachable_rests[new_rest] = new_cycles
            queue.append((new_rest, new_cycles))

# Помечаем недостижимые остатки для суммы N
for x in range(len(reachable_rests)):
    start_sum = (reachable_rests[x] * mod - (mod - x))
    if start_sum > N or reachable_rests[x] > full_cycles + 1:
        reachable_rests[x] = -1

sum_count = 1  # сумму 0 можно получить всегда

# Считаем количество достижимых сумм по остаткам
for x in range(len(reachable_rests)):
    # Исключаем недостижимые остатки
    if reachable_rests[x] < 0:
        continue

    # Проверяем достижимость итоговых остатков N % mod
    if x > 0 and x <= full_rest:
        sum_count += 1
    sum_count += full_cycles - reachable_rests[x] + 1

print(sum_count)

MAX_SIZE = 150  # Максимальный размер массива


number_of_prices = int(input())
if number_of_prices == 0:
    print(0)  # Если количество обедов равно 0, выводим 0 и выходим
    exit()
prices = [0] * MAX_SIZE  # Массив для цен обедов
for i in range(1, number_of_prices + 1):
    prices[i] = int(input())

# Инициализация динамического программирования
INF = MAX_SIZE * number_of_prices + 300  # Значение для инициализации
dp = [[INF] * MAX_SIZE for _ in range(MAX_SIZE)]  # Массив для хранения минимальных затрат
dp[0][0] = 0  # Начальное условие

# Вычисление минимальных затрат
for i in range(1, number_of_prices + 1):
    for j in range(i + 1):
        # Минимизируем значение dp[i][j]
        dp[i][j] = min(dp[i][j], dp[i - 1][j] + prices[i])

        # Если текущий элемент больше 100(купон), рассматриваем увеличение j
        if prices[i] > 100:
            dp[i][j + 1] = min(dp[i][j + 1], dp[i - 1][j] + prices[i])

        # Если j больше или равно 1, рассматриваем уменьшение j
        if j >= 1:
            dp[i][j - 1] = min(dp[i][j - 1], dp[i - 1][j])

# Минимальное значение в последней строке dp
minimum_result = INF
for j in range(number_of_prices + 1):
    minimum_result = min(minimum_result, dp[number_of_prices][j])

print(minimum_result)

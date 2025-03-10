import sys

def calculate(n, apexes):

    # Если вершина одна, выводим координату X этой вершины
    if n == 1:
        print(f"{apexes[0][0]:.6f}")
        return

    # Если вершины две, выводим координату центра линии, образованной двумя вершинами
    if n == 2:
        centerX = (apexes[0][0] + apexes[1][0]) / 2.0
        print(f"{centerX:.6f}")
        return

    # Находим площадь
    halfArea = calculate_polygon_area(apexes) / 2.0

    left = min(apex[0] for apex in apexes)  # Минимальная x-координата
    right = max(apex[0] for apex in apexes)  # Максимальная x-координата
    precision = 1e-7
    leftArea = 0.0  # Площадь левой части многоугольника
    mid = 0.0  # Текущая x-координата

    while True:
        mid = (left + right) / 2
        leftArea = calculate_left_area(apexes, mid)
        if abs(halfArea - leftArea) <= precision:
            break
        if leftArea < halfArea:
            left = mid  # Если площадь меньше, ищем вправо
        else:
            right = mid  # Если площадь больше или равна, ищем влево

    print(f"{(left + right) / 2:.6f}")

def calculate_polygon_area(apexes):
    area = 0.0
    for i in range(len(apexes)):
        j = (i + 1) % len(apexes)
        area += (apexes[i][0] * apexes[j][1] - apexes[j][0] * apexes[i][1])
    return abs(area) / 2.0

def calculate_left_area(apexes, x):
    area = 0.0
    n = len(apexes)

    for i in range(n):
        j = (i + 1) % n
        x1 = apexes[i][0]
        y1 = apexes[i][1]
        x2 = apexes[j][0]
        y2 = apexes[j][1]

        if x1 <= x and x2 <= x:
            area += (x2 - x1) * (y2 + y1) / 2.0
        elif x1 >= x and x2 >= x:
            continue
        else:
            intersectY = y1 + (y2 - y1) * (x - x1) / (x2 - x1)  # Находим y при пересечении
            if x1 < x:
                area += (x - x1) * (y1 + intersectY) / 2.0
            else:
                area += (x2 - x) * (intersectY + y2) / 2.0
    return abs(area)


n = int(input())  # количество вершин
apexes = [[0] * 2 for _ in range(n)]  # координаты вершин
for i in range(n):
     apexes[i] = list(map(int, input().split()))
calculate(n, apexes)
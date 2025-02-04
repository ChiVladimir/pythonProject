# https://code.mu/ru/python/tasker/stager/

# Весь код здесь и далее - это решение учебных задач, поэтому практически нигде не делаются необходимые валидации данных (при воде и/или обработке)

x = int(input())
if x < 0:
    print("Negative number")
else:
    print("Positive number")

if x%2 == 0:
    print("Even number")
else:
    print("Odd number")



x_X = str(input())
y_Y = str(input())
print (f"Length of the string is {len(x_X)}")
print (f"Last symbol of the string is {x_X[-1]}")
if x_X == y_Y:
    print("The first symbols is the same")
else:
    print("The first symbols is not the same")

if y_Y[-1] == "z":
    print (f"Last symbol of the string before {y_Y[-1]} is {y_Y[-2]}")
else:
    print(f"Last symbol of the string is not {y_Y[-1]}")



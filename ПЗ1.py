print('Задание 1')
print('Hello')

print()

print('Задание 2')
name = input('Введите имя: ')
print(f'Привет, {name}!')

print()

print('Задание 3')
num1 = float(input('Введите число: '))
num2 = float(input('Введите число: '))
print(f'Сумма чисел: {num1 + num2}')

print()

print('Задание 4')
num3 = float(input('Введите число: '))
num4 = float(input('Введите число: '))
print(f'Сумма: {num3 + num4}')
print(f'Вычитание: {num3 - num4}')
print(f'Умножение: {num3 * num4}')
try:
    print(f'Возведение в степень: {num3 ** num4}')
except:
    pass
try:
    print(f'Деление: {num3 / num4}')
    print(f'Целочисленное деление: {num3 // num4}')
    print(f'Остаток от деления: {num3 % num4}')
except:
    pass

print()

print('Задание 5')
num5 = int(input('Введите число: '))
if num5 % 2 == 0:
    print(f'Число {num5} - четное')
else:
    print(f'Число {num5} - нечетное')

print()

print('Задание 6')
num6 = int(input('Введите число: '))
if num6 > 0:
    print(f'Число {num6} - положительное')
elif num6 < 0:
    print(f'Число {num6} - отрицательное')
else:
    print(f'Число {num6} - ноль')

print()

print('Задание 7')
num7 = int(input('Введите число: '))
for i in range(11):
    print(f'{num7} * {i} = {num7 * i}')

print()

print('Задание 8')
num8 = int(input('Введите число: '))
factor = 1
for i in range(1, num8+1):
    factor *= i
print(f'Факториал {num8} = {factor}')

print()

print('Задание 9')
num9 = int(input('Введите число: '))
if num9>1 and all(num9%i != 0 for i in range(2, int(num9*0.5)+1)):
    print(f'Число {num9} - простое')
else:
    print(f'Число {num9} - не является простым')

print()

print('Задание 10')
nums = []
for i in range(3):
    nums.append(int(input('Введине число: ')))
print(f'{max(nums)} - наибольшее число')
print(f'{min(nums)} - наименьшее число')

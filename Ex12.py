# Дано два натуральных числа X и Y (X,Y≤1000), сумма этих чисел S и их произведение P. 
# Найти X и Y.
sum = int(input('Введите сумму чисел = '))
multi = int(input('Введите произведение чисел = '))
flag = 0
for i in range(sum):
    if i*(sum-i) == multi:
        print(i, sum-i)
        flag = 1
if flag == 0:
    print("Неверные условия")
    
#### 2.1[10]: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – 
# гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки 
# были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые
#  нужно перевернуть. Количество монет и их положение (0 или 1) пользователь вводит с 
# клавиатуры.

    # Примеры/Тесты:
    # Введите кол-во монет>? 5
    # Положение монеты 0: 0 или 1>? 1
    # ...
    # 1 0 1 1 0
    # Кол-во монет, чтобы перевернуть: 2

coins_number = int (input("Введите количество монеток: "))
print ("Далее вводите положение монеток, где 1 - решка, 0 - орел")
count_ud = 0
count_down = 0
for i in range (coins_number):
    temp = input(f"Положение {i+1} монетки: ")
    item = int (temp)
    if item == 1:
        count_ud +=1
    elif item == 0:
        count_down +=1
    else:
        print ("Вы ввели не корректное значение. програма зевершена")
        break
result = f"Вам нужно перевернуть {count_ud} монеток и все будет орлами вверх" if count_ud < count_down else f"Вам нужно перевернуть {count_down} монеток и все будет решкой вверх"
if count_ud == count_down: 
    result = "Количество решек и орлов одинаковое. Выбирай любые"
print (result)
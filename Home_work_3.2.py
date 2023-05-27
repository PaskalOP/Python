#### 3.2[18]: Требуется найти в списке целых чисел самый близкий по величине элемент к заданному числу X.  Пользователь вводит это
#  число с клавиатуры, список можно считать заданным. Введенное число не обязательно содержится в списке.

    # Примеры/Тесты:
    # Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 0
    # Output: 2
    # Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 9


list1 = [10, 5, 7, 3, 3, 2, 5, 7, 3, 8]
user_number = int(input("Введите число: "))
result_number = ""
differnt_dictionary = dict()
list_temp = sorted(list1)

print(list1)
min = 100000
if user_number>=list_temp [len(list_temp )-1]:
    result_number =list_temp [len(list_temp )-1]
else:
    for item in list1:
        differnt_dictionary [item] = user_number-item if user_number-item>=0 else -(user_number-item)
    for key,value in  differnt_dictionary.items():
        if value<min:
            min=value
            result_number = key

print(result_number)
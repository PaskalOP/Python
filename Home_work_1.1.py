# 1.1[2]. Найдите сумму цифр трехзначного числа. Используйте f-строки чтобы оформить 
# красивый вывод
# Например для числа 145 сумма цифр будет 10: 1 + 4 + 5
# Примеры/Тесты:
# 123 >>> Сумма чисел числа 123 равна 6
# 100 >>> Сумма чисел числа 100 равна 1
# ```(*)``` **Усложнение.** Решите для числа произвольной разрядности: произвольное количество цифр в числе.
# ```(**)``` **Усложнение.** Для числа произвольной разрядности добавить в вывод строку с числами, например так:
# 13579 >>> Сумма чисел числа 13579 равна 25(1 + 3 + 5 + 7 + 9)
# Совет: Для этого используйте конкатенацию строк и срезы 

number_string=input("Введите число ")
number = int(number_string)
sum=0
count =0

while (count<len(number_string)):
     sum += number%10
     number//=10
     count+=1

string_print = ""
for i in range(len(number_string)):
     if i!= len(number_string) -1:
         string_print+= number_string[i] + " + "
     else:
          string_print+= number_string[i]

print (f"Сумма цифер числа {number_string} равна {sum} ({string_print}) ")




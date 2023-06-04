#### 5.2[28]: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных
#  чисел. Из всех арифметических операций допускаются только +1 и -1. Циклы использовать нельзя
    
	# Примеры/Тесты:
    # <function_name>(0,0) -> 0
    # <function_name>(0,2) -> 2
    # <function_name>(3,0) -> 3

def recursiv_sum (a: int, b:int):
    result_sum = 0
    if a==0:
        result_sum = b
    elif b==0:
        result_sum = a
    else:
        result_sum = recursiv_sum(a-1,b+1)
    
    return result_sum
   
print(recursiv_sum(5,15))
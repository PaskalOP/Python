# №5.1[31]. Последовательностью Фибоначчи называется последовательность чисел 
# a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# https://ru.wikipedia.org/wiki/Числа_Фибоначчи
# Требуется найти N-е число Фибоначчи. Напишите рекурсивную функцию. Обратите
#  внимание, что функция должна возвращать число.
# Примеры/Тесты:
#     <function_name>(0) -> 0
#     <function_name>(2) -> 1
#     <function_name>(9) -> 34

def Fibonacci(m):
    if m == 0:
        return 0
    elif m == 1:
        return 1
    else:
        return Fibonacci(m-2)+Fibonacci(m-1)
    
print(Fibonacci(9))
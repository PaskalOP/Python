#### 5.1[26]: Напишите рекурсивную функцию для возведения числа a в степень b.
#  Разрешается использовать только операцию умножения. Циклы использовать нельзя

    # Примеры/Тесты:
    # <function_name>(2,0) -> 1
    # <function_name>(2,1) -> 2
    # <function_name>(2,3) -> 8
    # <function_name>(2,4) -> 16

def exponentiation (a: int, b:int):
    resalt = 0
    if b==0:
        resalt =1
    else:
        resalt = a*exponentiation(a,b-1)
    
    return resalt

print (exponentiation(2,4))

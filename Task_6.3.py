# №6.3[43] Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу, образуют одну пару, которую 
# необходимо посчитать.
# Напишите функцию
#     Аргументы: список целых чисел
#     Возвращает: кол-во пар

# Примеры/Тесты:
#     <function_name>([1, 2, 3, 2, 3]) -> 2
#     <function_name>([1, 2, 3, 2, 3, 3, 2, 4]) -> 6

list1 = [1, 2, 3, 2, 3]
list2 = [1, 2, 3, 2, 3, 3, 2, 4]

def count_pairs(lst1:list):
    result=0
    for idx in range(len(lst1)):
        for idx2 in range(idx+1,len(lst1)):
            if lst1[idx]==lst1[idx2]:
                result+=1        
    return result

# def count_pairs(lst1:list):
#     result=0
#     for idx in range(len(lst1)):
#         result+=lst1[idx+1:].count(lst1[idx])
#     return result

totalResult1 = count_pairs(list1)
totalResult2 = count_pairs(list2)
print(totalResult1)
print(totalResult2)
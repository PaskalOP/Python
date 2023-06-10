# Дан список. Нужно выбрать только четные и составить список  пар: число - его квадрат

list1 = [1, 2, 3, 5, 8, 15, 23, 38]
def mult (list_num:list) -> list:
    result_list = [(item,item*item,) for item in list_num if item %2==0 ]
    return result_list

print (mult(list1))
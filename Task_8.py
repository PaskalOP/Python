# №8.1[49]. Создать телефонный справочник с возможностью импорта и экспорта данных в формате .csv
# Информация о человеке:
#     Фамилия, Имя, Телефон, Описание
# Корректность и уникальность данных не обязательны.
# Функционал программы
# 1) телефонный справочник хранится в памяти в процессе выполнения кода. 
#     Выберите наиболее удобную структуру данных для хранения справочника.
# 2) CRUD: Create, Read, Update, Delete
#     Create: Создание новой записи в справочнике: ввод всех полей новой записи, занесение ее в справочник.
#     Read: он же Select. Выбор записей, удовлетворяющих заданном фильтру: по первой части фамилии человека. Берем первое совпадение по фамилии.
#     Update: Изменение полей выбранной записи. Выбор записи как и в Read, заполнение новыми значениями.
#     Delete: Удаление записи из справочника. Выбор - как в Read.
# 3) экспорт данных в текстовый файл формата csv
# 4) импорт данных из текстового файла формата csv


# Используйте функции для реализации значимых действий в программе

# Усложнение.

# - Сделать тесты для функций
# - Разделить на model-view-controller

# user = ["second_name","first_name","phone","discription"]
# phone_dir = {1:["second_name","first_name","phone","discription"], 2:["second_name","first_name","phone","discription"]}
# key_count - счетчик id
from os.path import join, abspath, dirname

phone_direct = {1: ['Иванов',   'Иван',  '+7(xxx)xxx-xx-xx', 'desription_Иванов'], 
2: ['Петров',   'Петр',  '+7(---)xxx-xx-xx', 'desription_Петров'], 
3: ['Соколов',  'Илья',  '+7(---)---------', 'desription_Соколов'], 
4: ['Павельев', 'Андрей','+7(***)***-**-**', 'desription_Павельев'], 
5: ['Пешехов',  'Антон', '+7++++++++++',     'desription_Пешехов'], 
6: ['Сааков',   'Илья',  '+7(+++)+++-++-++', 'desription_Сааков'], 
}

def Input_Users()->list:
    user=[]
    user.append(input("Input first name "))
    user.append(input("Input second name "))
    user.append(input("Input phone "))
    user.append(input("Input discription "))
    
    return user


def create( phone_dir_local: dict, idc: int,  user:list)->dict:
    idc += 1
    phone_dir_local[idc] = user
    return phone_dir_local, idc

# user1 = ["second_name1","first_name1","phone1","discription1"]
# user2 = ["second_name2","first_name2","phone2","discription2"]

# phone_dir, key_count=create(phone_dir,key_count,user1)
# phone_dir, key_count=create(phone_dir,key_count,user2)
# print(phone_dir)

def export_phone_dir(phone_dir: dict, file_name: str):
    MAIN_DIR = abspath(dirname(__file__))
    full_name = join(MAIN_DIR, file_name+'.txt')
    with open(full_name, mode='w', encoding='utf-8') as file:
        for idc, user in phone_dir.items():
            file.write(f"{idc}#{user[0]}#{user[1]}#{user[2]}#{user[3]}\n")

def import_dir(file_name: str):
    with open (file_name, "rt") as dir_from_file:
        import_direction = dict()
        for item in dir_from_file:
            temp_user = item.strip().split("#")
            key = int(temp_user[0])
            import_direction [key]=temp_user[1:]
        return import_direction

def search_user(phone_dir: dict, searching: str) -> int:
    for idc, user in phone_dir.items():
        
        if user[0].startswith(searching):
            return idc, user

def print_dict(phone_dir: dict):
    for idc, user in phone_dir.items():
        print(f"{idc}: {user[0]} {user[3]} {user[2]} {user[3]}")


def delete (phone_dir: dict, searching: str):
    for idc, user in phone_dir.items():
        if user[0].startswith(searching):
            del phone_dir[idc]
            break
    return phone_dir

def update (phone_dir: dict, searching: str):
    for idc, user in phone_dir.items():
        if user[0].startswith(searching):
            new_second_name = input ("Измени фамилию ")
            new_name = input ("Измени имя ")
            new_phone = input ("Измени номер ")
            new_discrition = input ("Измени описание ")
            if len(new_second_name)>=1:
                user[0]=new_second_name
            if len(new_name)>=1:
                user [1] =new_name
            if len(new_phone)>=1:
                user[2] = new_phone 
            if len(new_discrition)>=1:
                user [3] = new_discrition
            break
    return phone_dir

def menu (phone_dir:dict ):
    print("Введите 1, если хотите ввести пользователя ")
    print("Введите 2, если хотите распечатать справочник ")
    print("Введите 3 для экспорта")
    print("Введите 4 для поиска")
    print ("Введите 5, чтоб удалить элемент")
    print ("Введите 6, чтоб редактировать элемент")
    print ("Введите 7, если ходите импортировать данный из фаила ")
    key_count =0
    number =0
    fio =""
    while True:
        num = int(input("Выберите операцию "))
        if num == 0:
            break
        if (num ==1):
           user = Input_Users()
           phone_dir, key_count = create(phone_dir,key_count,user)
        if num == 2:
            print (phone_dir)
        if num == 3:
            file_name = input("Выберите имя файла ")
            export_phone_dir(phone_dir, file_name)
        if num == 4:
            searching = input("Кого ищем? ")
            number, fio = search_user(phone_dir,searching)
            print (f"Пользователь {fio} находится под номером {number}" )
        if num == 5:
            remove_name = input("Кого будем удалять?")
            phone_dir =  delete (phone_dir,remove_name)
            print("Обновленный список")
            print (phone_dir)
        if num == 6:
            change_element = input ("Введите, кого будем редактировать ")
            phone_dir = update (phone_dir,change_element )
            print (phone_dir)
        if num == 7:
            import_file_name = input ("Введите название фаила, который будем импортировать ")
            phone_dir = import_dir(import_file_name )
            print (phone_dir)


# print(update(phone_direct, "Соко"))
# print(delete(phone_direct,"Соко"))
# export_phone_dir(phone_dir, "phones")
# print(search_user(phone_direct, "Петр"))
# print (import_dir("phones.txt"))
# print(Input_Users())
menu (phone_direct)

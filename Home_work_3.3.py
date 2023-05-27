# 3.3[20]: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.

# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.

# Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово,
# которое содержит либо только английские, либо только русские буквы и заранее известно 
# какой алфавит надо использовать.

#     Примеры/Тесты:
#     Input:   ноутбук
#     Output:  12
    
#     Input:   notebook
#     Output:  14

# ```(*)``` **Примечание.**
# Подумайте о том какие структуры данных здесь наиболее удобно использовать, чтобы просто проверять в 
# какую группу попадает буква, а также просто накапливать сумму очков.

one_poin_en = {"A", "E", "I", "O", "U", "L", "N", "S", "T", "R"}
two_point_en = {"D", "G"}
three_point_en = {"B", "C", "M", "P"}
four_point_en = {"F", "H", "V", "W", "Y"}
five_point_en = {"K"}
eight_point_en = {"J", "X"}
ten_point_en = {"Q", "Z"}
# english_letters =(one_poin_en,two_point_en, three_point_en, four_point_en, five_point_en, eight_point_en,ten_point_en,)

one_poin_ru = {"А", 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', "Т"}
two_point_ru = {"Д", 'К', 'Л', 'М', 'П', "У"}
three_point_ru = {"Б", 'Г', 'Ё', 'Ь', "Я"}
four_point_ru = {"Й", "Ы"}
five_point_ru = {"Ж", 'З', 'Х', 'Ц', "Ч"}
eight_point_ru = {"Ш", 'Э', "Ю"}
ten_point_ru = {"Ф", "Щ", "Ъ"}
# rusian_letters = (one_poin_ru,two_point_ru,three_point_ru,four_point_ru,five_point_ru,eight_point_ru,ten_point_ru)

language = int (input("Если вы используете русский язык, введите 1. Если английский, то введите 2"))
world_user = input ("Введите нужное слово: ")
world = world_user.upper()

count = 0
if language == 1:
    i=0
    while(i<len(world)):
        for item in one_poin_ru:
            if world [i] ==item:
                count +=1
                break
        for item in two_point_ru:
            if world [i] ==item:
                count +=2
                break
        for item in three_point_ru:
            if world [i] ==item:
                count +=3
                break
        for item in four_point_ru:
            if world [i] ==item:
                count +=4
                break
        for item in five_point_ru:
            if world [i] ==item:
                count +=5
                break
        for item in eight_point_ru:
            if world [i] ==item:
                count +=8
                break
        for item in ten_point_ru:
            if world [i] ==item:
                count +=10
                break
        i+=1


if language == 2:
    i=0
    while(i<len(world)):
        for item in one_poin_en:
            if world [i] ==item:
                count +=1
                break
        for item in two_point_en:
            if world [i] ==item:
                count +=2
                break
        for item in three_point_en:
            if world [i] ==item:
                count +=3
                break
        for item in four_point_en:
            if world [i] ==item:
                count +=4
                break
        for item in five_point_en:
            if world [i] ==item:
                count +=5
                break
        for item in eight_point_en:
            if world [i] ==item:
                count +=8
                break
        for item in ten_point_en:
            if world [i] ==item:
                count +=10
                break
        i+=1

print (f"Количество баллов этого слова = {count}")


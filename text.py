import random
n = int(input("Введите кол-во монет для броска: ")) # размер массива 
random_1 = random.randrange(n) # случайное число для "Орла"
remndr = n - random_1 # остаток числа random_1 для "Решки"
t = [] # пустой список
for i in range(random_1): # Цикл для загрузки значений
    t.append("Орел") # добавление значения 
for i in range(remndr): # Цикл для загрузки значений
    t.append("Решка") # добавление значения 
random.shuffle(t) # Перемешка списка
print(f"Ваш выброс: {t} ") # Вывод всех значений списка в перемешанном порядке
eagle = t.count("Орел") # Подсчет
tails = t.count("Решка") # Подсчет
print(f"Требуется перевернуть {eagle} монет с Орлом") # ф- строка с выводом орла
print("Для обратного результата") # доп инфо
print(f"Требуется перевернуть {tails} монет с Решкой")# ф- строка с выводом решки
 

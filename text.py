import random
import math
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

""""""
# Exersize 2
#Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# Пример --- 7, 10 -> 2, 5 (2 + 5 == 7; 2 * 5 == 10)

x = random.randint(1,1000)
y = random.randint(1,1000)
s = x + y
p = x * y
print(f"Cумма 1-ого числа = {s}")
print(f"Произведение 2-ого числа = {p}")
x_1 = s*s
x_2 = p * 4
discrmt = x_1 - x_2
root = int(math.sqrt(discrmt))
result_x = int((s + root) / 2)
result_y = int((s - root) / 2)
try_end = 3
while try_end !=0:
    quest = input("Чему равен x?")
    quest_1 = input("Чему равен y?")
    try_end = try_end - 1
    if try_end > 0:
        print("Думай лучше")
        print(f"У вас осталось {try_end} попыток")
    if quest == x and quest_1 == y:
        print("УГАДАЛ ТЫ УМНИЧКА")
        print(f"Загаданный x={result_x}")
        print(f"Загаданный y={result_y}")
    if quest !=x and quest_1 !=y and try_end==0:
        print("Не угадал! >_<")
        print(f"Загаданный x={result_x}")
        print(f"Загаданный y={result_y}")
        
#Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
#50 -> 1, 2, 4, 8, 16, 32

n = int(input("Введите максимальное число для рассчета"))
dot = 1
result_numb = []

while dot <= n:
    result_numb.append(dot)
    dot *= 2
print(result_numb)
    
    

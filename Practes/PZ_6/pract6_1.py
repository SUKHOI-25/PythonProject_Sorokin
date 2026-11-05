from random import randint

# Дан целочисленный список размера N. Проверить, чередуются ли в нем четные и
# нечетные числа. Если чередуются, то вывести 0, если нет, то вывести порядковый
# номер первого элемента, нарушающего закономерность.


def error_handler(work_permit): # обработчик базовых ошибок в ведении с руки
    while True:
        try:
            return int(input(work_permit))
        except ValueError:
            print("Это не целое число")
        except EOFError:
            print("Для выхода нажмите CTRL+C\nCTRL+D для линукс и CTRL+Z на виндовс не прерывают цикл")

print("-----Рулетка списка-----")

n = error_handler("Введите размер списка: ")

de_listo = []

for i in range(n):
    a = randint(-100,100)
    de_listo.append(a)

last_i = de_listo[0] # записываем первое число списка для сравнения

print(de_listo)

for i in range(1,len(de_listo)): # от 1 тк индекс 0 берет на себя last_i
    if de_listo[i]%2==last_i%2: # тут было много слез
        print(f"Цикл сломало число - {de_listo[i]}")
        break
    else:
        last_i=de_listo[i]
        continue
else:
    print(0)
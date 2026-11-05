from random import randint


# Даны два списка A и B одинакового размера N. Сформировать новый список C того
# же размера, каждый элемент которого равен максимальному из элементов списков
# A и B.


def error_handler(work_permit): # обработчик базовых ошибок в ведении с руки
    while True:
        try:
            return int(input(work_permit))
        except ValueError:
            print("Это не целое число")
        except EOFError:
            print("Для выхода нажмите CTRL+C\nCTRL+D для линукс и CTRL+Z на виндовс не прерывают цикл")


n = error_handler("Введите размер списков: ")

de_list0 = []
de_list1 = []
de_perfectlisto = []

for i in range(n):
    a = randint(-100,100)
    de_list0.append(a)
    b = randint(-100,100)
    de_list1.append(b)

print(f"Лист 1: {de_list0}")
print(f"Лист 2: {de_list1}")

for i in range(len(de_list0)):
    if de_list0[i]>de_list1[i]:
        de_perfectlisto.append(de_list0[i])
    elif de_list1[i]>de_list0[i]:
        de_perfectlisto.append(de_list1[i])
    else:
        continue

print(f"Идеальный лист: {de_perfectlisto}")
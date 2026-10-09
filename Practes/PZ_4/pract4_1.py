# Даны два целых числа A и B (A < B). Вывести в порядке возрастания все целые
# числа, расположенные между A и B (включая сами числа A и B), а также количество
# N этих чисел.


def error_handler(work_permit): # обработчик базовых ошибок в ведении с руки
    while True:
        try:
            return int(input(work_permit))
        except ValueError:
            print("Это не целое число")
        except EOFError:
            print("Для выхода нажмите CTRL+C\nCTRL+D для линукс и CTRL+Z на виндовс не прерывают цикл")


a = error_handler("Введите число А: ")
b = error_handler("Введите число B: ")
for i in range(a,b+1):
    print(f"{i}")
print(f"N чисел включая А и В: {b-a+1}\nНе включая A и B: {b-a-1}")
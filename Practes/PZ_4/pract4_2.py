# Дано целое число N (>0). Если оно является степенью числа 3, то вывести TRUE,
# если не является — вывести FALSE.


def error_handler(work_permit): # обработчик базовых ошибок в ведении с руки
    while True:
        try:
            return int(input(work_permit))
        except ValueError:
            print("Это не целое число")
        except EOFError:
            print("Для выхода нажмите CTRL+C\nCTRL+D для линукс и CTRL+Z на виндовс не прерывают цикл")


n = error_handler("Введите число N: ")

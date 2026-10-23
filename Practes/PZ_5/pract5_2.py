# Описать функцию DigitCountSum(K, C, S), находящую количество C цифр целого
# положительного числа K, а также их сумму S (K — входной, C и S — выходные
# параметры целого типа). С помощью этой функции найти количество и сумму цифр
# для каждого из пяти данных целых чисел.

def error_handler(work_permit): # обработчик базовых ошибок в ведении с руки
    while True:
        try:
            return int(input(work_permit))
        except ValueError:
            print("Это не целое число")
        except EOFError:
            print("Для выхода нажмите CTRL+C\nCTRL+D для линукс и CTRL+Z на виндовс не прерывают цикл")

k=error_handler("Введите число k ")


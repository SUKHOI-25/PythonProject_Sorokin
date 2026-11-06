# Дано целое число N (>0) и строка S. Преобразовать строку S в строку длины N
# следующим образом: если длина строки S больше N, то отбросить первые символы,
# если длина строки S меньше N, то в ее начало добавить символы «.» (точка).


def error_handler(work_permit): # обработчик базовых ошибок в ведении с руки
    while True:
        try:
            return int(input(work_permit))
        except ValueError:
            print("Это не целое число")
        except EOFError:
            print("Для выхода нажмите CTRL+C\nCTRL+D для линукс и CTRL+Z на виндовс не прерывают цикл")


thestr = "Банан арбуз коконут"
lenstr = len(thestr)
print(f"Строка длинной {lenstr} : {thestr}")


while True:
    n = error_handler("Введите число >0 : ")
    if n>0:
        break
    else:
        print("Число должно быть больше нуля")
        continue


if lenstr>n:
    print(thestr[n:])
elif lenstr<n:
    print(f"{"."*(n-lenstr)}{thestr}")
else:
    print(thestr)

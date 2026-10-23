def error_handler(work_permit): # обработчик базовых ошибок в ведении с руки
    while True:
        try:
            return int(input(work_permit))
        except ValueError:
            print("Это не целое число")
        except EOFError:
            print("Для выхода нажмите CTRL+C\nCTRL+D для линукс и CTRL+Z на виндовс не прерывают цикл")

def summirovanie(n,m):
    summa=0
    for i in range(n,m+1):
        summa+=i
    return summa

n=error_handler("Введите цисло n ")
m=error_handler("Введите цисло m ")

print(f"Ответ : {summirovanie(n,m)}")
#Даны числа х, у. Проверить истинность высказывания: «Точка с координатами (х, у) лежит во второй координатной четверти».
def error_handler(work_permit):
    while True:
        try:
            return int(input(work_permit))
        except ValueError:
            print("Это не целое число")
        except EOFError:
            print("Для выхода нажмите CTRL+C\nCTRL+D для линукс и CTRL+Z на виндовс не прерывают цикл")
try:
    x = error_handler("Введите x координату: ")
    y = error_handler("Введите y координату: ")
    print(x<0 and y>0)
except KeyboardInterrupt:
    print("\n\nПрограмма прервана пользователем")
# Даны координаты поля шахматной доски х, у (целые числа, лежащие в диапазоне 1-8). 
# Учитывая, что левое нижнее поле доски (1,1) является черным, проверить истинность 
# высказывания: «Данное поле является белым»


def error_handler(work_permit):
    while True:
        try:
            user_input=int(input(work_permit))
            if user_input<1 or user_input>8:
                print("\nВводить целые числа, лежащие в диапазоне 1-8") # Доп обработчик чисел
                continue
            else:
                return user_input
        except ValueError:
            print("\nЭто не целое число")
        except EOFError:
            print("\nДля выхода нажмите CTRL+C\nCTRL+D для линукс и CTRL+Z на виндовс не прерывают цикл")


try:
    x = error_handler("Введите x координату (целые числа, лежащие в диапазоне 1-8) : ")
    y = error_handler("Введите y координату (целые числа, лежащие в диапазоне 1-8) : ")

    print(f"Данное поле является белым: {(x%2==0 and y%2!=0) or (x%2!=0 and y%2==0)}") # XOR
except KeyboardInterrupt:
    print("\n\nПрограмма прервана пользователем")
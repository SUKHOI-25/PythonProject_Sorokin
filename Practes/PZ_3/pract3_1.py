try:
    while True:
        try:
            x = int(input("Введите x координату : "))
            y = int(input("Введите y координату : "))

            print(True) if x<0 and y>0 else print(False)
            break
        except ValueError:
            print("Это не целое число")
        except EOFError: #ctrl+d пустой ввод (на винде ctrl+z)
            print("Что-то натыкали в консоли")
except KeyboardInterrupt: #ctrl+c жесткое прерывание (перерывание через ctrl+z не обрабатывается)
    print("\n\nПрограмма прервана пользователем")
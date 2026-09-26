try:
    while True:
        try:
            n = int(input("Введите количество секунд прошедших с начала суток: "))
            if n > 0:
                n %= 86400 # удаляем день если секунд больше чем в 24 часах
                hours, remains = divmod(n, 3600) #hours-целая часть от деления (//), remains-остаток от деления в секундах (%)
                minutes, seconds = divmod(remains, 60)
                print(f"h:{hours:02d}, m:{minutes:02d}, s:{seconds:02d}")
                break
            elif n == 0:
                print("Ни часов ни минут ни секунд не прошло")
                continue
            elif n < 0:
                print("Некорректное время")
                continue
        except ValueError:
            print("Это не целое число")
        except EOFError: #ctrl+d пустой ввод (на винде ctrl+z)
            print("Что-то натыкали в консоли")
except KeyboardInterrupt: #ctrl+c жесткое прерывание (перерывание через ctrl+z не обрабатывается)
    print("\n\nПрограмма прервана пользователем")
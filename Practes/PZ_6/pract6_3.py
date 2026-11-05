from random import randint


# Даны множества A и B, состоящие соответственно из N1 и N2 точек (точки заданы
# своими координатами x, у). Найти минимальное расстояние между точками этих
# множеств и сами точки, расположенные на этом расстоянии (вначале выводится
# точка из множества A, затем точка из множества B).
# Расстояние R между точками с координатами (x1, y1) и (x2, у2) вычисляется по формуле:
# R = √(x2 – x1)2 + (у2 – y1)2
# Для хранения данных о каждом наборе точек следует использовать по два списка: первый
# список для хранения абсцисс, второй — для хранения ординат.


def error_handler(work_permit): # обработчик базовых ошибок в ведении с руки
    while True:
        try:
            return int(input(work_permit))
        except ValueError:
            print("Это не целое число")
        except EOFError:
            print("Для выхода нажмите CTRL+C\nCTRL+D для линукс и CTRL+Z на виндовс не прерывают цикл")


n1 = error_handler("Введите колво точек списка A : ")
n2 = error_handler("Введите колво точек списка B : ")

A_xs = []
A_ys = []
B_xs = []
B_ys = []
best_r = 0
lastB_r = 100000
lastB_combo = []

for i in range(n1):
    a = randint(-100,100)
    A_xs.append(a)
    b = randint(-100,100)
    A_ys.append(b)

for i in range(n2):
    a = randint(-100,100)
    B_xs.append(a)
    b = randint(-100,100)
    B_ys.append(b)

print(f"A(x) : {A_xs},\nA(y) : {A_ys},")
print(f"B(x) : {B_xs},\nB(y) : {B_ys}")


for i in range(n1): # переберает все значения множества B
    for j in range(n2): # перебирает все значения множества А
        best_r = ((B_xs[j] - A_xs[i])**2 + (B_ys[j] - A_ys[i])**2)**0.5
        if best_r<lastB_r:
            lastB_r = best_r
            lastB_combo = []
            lastB_combo.extend([A_xs[i],A_ys[i],B_xs[j],B_ys[j]])
    

# print(f"best_r = {best_r}, lastB_r = {lastB_r}, lastB_combo = {lastB_combo}") #для отладки
print(f"Наименьшее расстояние = {lastB_r},\nКомбо ближайших точек(вид xAyAxByB) = {lastB_combo}")
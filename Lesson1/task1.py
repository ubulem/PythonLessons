# coding=utf-8
x = int(raw_input("Введите целое число от 1 до 9: "))
if x in range(1, 4):  # формирует список [1,2,3], тем самым мы проверяем, что x входит в этот список
    s = raw_input("Введите строку: ")
    n = int(raw_input("Введите число повторов строки: "))
    res = ""  # инициализируем пустую строку, чтобы в цикле прибавлять к ней введенную s
    for i in range(n):  # задаем цикл от 0 до n-1, таким образом он выполнится n раз
        res += s
    print (res)
elif x in range(4, 7):
    m = int(raw_input("Введите степень: "))
    res = 1
    for i in range(m):
        res *= x
    print (res)
elif x in range(7, 10):
    for i in range(10):
        x += 1
        print (str(x))
else:
    print ("Ошибка ввода")

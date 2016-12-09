# coding=utf-8
def from_1_to_3(a):
    return a in range(1, 4)


def from_4_to_6(a):
    return a in range(4, 7)


def from_7_to_9(a):
    return a in range(7, 10)


# task 1
x = int(raw_input("Введите целое число от 1 до 9: "))
if from_1_to_3(x):
    s = raw_input("Введите строку: ")
    n = int(raw_input("Введите число повторов строки: "))
    res = ""  # инициализируем пустую строку, чтобы в цикле прибавлять к ней введенную s
    for i in range(n):  # задаем цикл от 0 до n-1, таким образом он выполнится n раз
        res += s
    print (res)
elif from_4_to_6(x):
    m = int(raw_input("Введите степень: "))
    res = 1
    for i in range(m):
        res *= x
    print (res)
elif from_7_to_9(x):
    for i in range(10):
        x += 1
        print (str(x))
else:
    print ("Ошибка ввода")


# task 2
def kindergarten(age):
    return age in range(7)


def school(age):
    return age in range(7, 18)


def university(age):
    return age in range(18, 25)


def work(age):
    return age in range(25, 60)


def retirement(age):
    return age in range(60, 120)


def not_human(age):
    retirement(age < 0 or age > 120)


print ("Общество в начале XXI века")
your_age = int(raw_input("Введите свой возраст: "))
if kindergarten(your_age):
    print ("Вам в детский сад")
elif school(your_age):
    print ("Вам в школу")
elif university(your_age):
    print ("Вам в профессиональное учебное заведение")
elif work(your_age):
    print ("Вам на работу")
elif retirement(your_age):
    print ("Вам предоставляется выбор")
elif not_human(your_age):
    print ("Ошибка! Это программа для людей!")

# coding=utf-8
user_word = raw_input("Введите слово: ")
user_str = raw_input("Введите строку: ")
pos = user_str.find(user_word)
if pos == -1:
    print ("Строка не содержит такого слова")
else:
    print ("Ваше слово начинается с " + str(pos) + " позиции")

# coding=utf-8
s = "Hello!World!How!Are You!Doing?"
delimiter = raw_input("Введите разделитель слов: ")
words_list = s.split(delimiter)  # то же самое что и в первом задании только разделитель - ;
print min(words_list, key=len)

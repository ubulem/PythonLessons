# coding=utf-8
s = "Lorem ipsum dolor sit amet consectetur adipiscing elit"
words_list = s.split()  # делим строку на список слов, разделитель - пробел
print max(words_list, key=len)  # производим поиск максимума по критерию длины слова - то есть самого длинного слова

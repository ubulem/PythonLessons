# coding=utf-8
s = "Duis;aute;irure;dolor;in;reprehenderit;in;voluptate;velit;esse;cillum;dolore;eu;fugiat;nulla;pariatur"
words_list = s.split(';')  # то же самое что и в первом задании только разделитель - ;
print max(words_list, key=len)

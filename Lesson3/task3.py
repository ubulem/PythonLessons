# coding=utf-8
def words_length(s):
    for word in s.split():
        print (word + " - " + str(len(word)))


user_str = raw_input("Введите строку: ")
words_length(user_str)

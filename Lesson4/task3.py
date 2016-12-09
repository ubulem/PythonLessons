# coding=utf-8
import random


def magic_ball():
    answers = ["Бесспорно",
               "Никаких сомнений",
               "Определенно да",
               "Вероятнее всего",
               "Хорошие перспективы",
               "Пока не ясно, попробуйте снова",
               "Спроси позже",
               "Ответ - нет",
               "По моим данным - нет"]
    index = random.randint(0, 8)
    return answers[index]


question = raw_input("Введите вопрос: ")
print (question + " - " + magic_ball())

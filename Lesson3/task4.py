# coding=utf-8
def successive_degree(*args):
    prev = 1
    for i in args:
        res = i ** prev
        prev = i
        print (res)


successive_degree(2, 4, 1, 5, 8, 3)

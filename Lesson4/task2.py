# coding=utf-8
import datetime
import os

path_input = raw_input("Введите путь к папке: ")

try:
    os.chdir(path_input)
    file_input = raw_input("Введите путь к папке/файлу: ")

    if os.path.exists(file_input):
        print ("Full path: " + os.path.abspath(file_input))
        print ("Size: " + str(os.path.getsize(file_input)))
        if os.path.isfile(file_input):
            print "Type: file"
        else:
            print "Type: directory"
        print("Created time: " +
              datetime.datetime.fromtimestamp(
                  os.path.getctime(file_input)
              ).strftime('%d-%m-%Y %H:%M:%S'))
        print("Modified time: " +
              datetime.datetime.fromtimestamp(
                  os.path.getmtime(file_input)
              ).strftime('%d-%m-%Y %H:%M:%S'))
    else:
        print ("File or folder not found")

except OSError:
    print "There is no such a directory. \nPlease provide the valid path."

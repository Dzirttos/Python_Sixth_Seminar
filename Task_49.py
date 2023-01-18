# Задача № 49
# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - 
# данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной
# 1 - Показать все записи
# 2 - Найти запись по имени
# 3 - Найти запись по телефону
# 4 - Добавить новый контакт
# 5 - Удалить контакт
# 6 - Выход


import os
os.system('cls')

telDict = 'tel.txt'

def printAll(file_name):
    # Показать все записи
    show = open(file_name, 'r', encoding='utf8')
    print(show.read())

def readFile(file_name):
    # приобразование данных в массив
    result = []
    with open(file_name, 'r+', encoding='utf8') as data:
        for line in data:
            result.append(line.split(','))
    return result

def nameSearch(dictArray):
    # поиск по имени
    name = ' ' + input('Введите имя для поиска: ')
    for i in dictArray:
        if i[1] == name:
                print(i[0]+','+i[1]+','+i[2]+','+ i[3])

def telSearch(userList):
    # поиск по телефону
    telNumber = ' ' + input('Введите номер телефона для поиска: ') + '\n'
    for i in userList:
        if i[3] == telNumber: 
           print(i[0]+','+i[1]+','+i[2]+','+ i[3])

def addData(file_name):
    # Добавление контакта
    new_data = input("Введите, пожалуйста, новые данные через запятую и пробел (', '): ")
    with open(file_name, 'a', encoding='utf8') as data:
        data.writelines(new_data + '\n')

def deleteData(file_name):
    # удаление записи
    data_to_delete = input("Удаление всех данных по конкретному человеку возможно по фамилии. Введите, пожалуйста, Фамилию того человека, чьи записи желаете удалить: ")
    s = ""
    with open(file_name, "r", encoding="utf8") as data:
        for line in data:
            if data_to_delete in line:
                continue
            s += line

    with open(file_name, "w", encoding="utf8") as data:
        data.write(s)
    
def default():
    # Вывод, если ошибка
    print("\033[31mДанный справочник не предусматривает ввод букв или цифр, отличных от указанных. Пожалуйста, проверьте ввод!")

print("Добрый день! Добро пожаловть в псевдоспраочник! \nДля продолжения выберете итересующую Вас категорию: \n1 - Показать все записи \n2 - Найти запись по имени \n3 - Найти запись по телефону \n4 - Добавить новый контакт \n5 - Удалить контакт \n6 - Выход \n ") 
userAnswer = input('Введите цифру: ')
os.system('cls')
match userAnswer:
        case "1": 
            printAll(telDict)

        case "2":
            nameSearch(readFile(telDict))
            
        case "3":
            telSearch(readFile(telDict))
        
        case "4":
            addData(telDict)
            
        case "5":
            deleteData(telDict)

        case "6":
            exit(0)

        case _:
            default()
        
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
# 6 - Изменить номер телефона у контакта
# 7 - Выход


import os
os.system('cls')

telDict = 'tel.txt'

def printAll(file_name):
    # Показать все записи
    show = open(file_name)
    print(show.read())

def readFile(file_name):
    # приобразование данных в массив
    result = []
    with open(file_name, 'r+') as data:
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
    for user in userList:
        if user[3] == telNumber: 
           print(user[0]+','+user[1]+','+user[2]+','+ user[3])



def writeFile(file_name):
    with open(file_name, 'a') as data:
        data.writelines('niggazzz' + '\n')





# writeFile(fileName)
print(readFile(telDict))
# '\n'
# findUses(readFile(telDict))


print("Добрый день! Добро пожаловть в псевдоспраочник! \nДля продолжения выберете итересующую Вас категорию: \n1 - Показать все записи \n2 - Найти запись по вхождению частей имени \n3 - Найти запись по телефону \n4 - Добавить новый контакт \n5 - Удалить контакт \n6 - Изменить номер телефона у контакта \n7 - Выход \n ") 
userAnswer = input('Введите цифру: ')
os.system('cls')
match userAnswer:
        case "1": 
            printAll(telDict)

        case "2":
            nameSearch(readFile(telDict))
            
        case "3":
            telSearch(readFile(telDict))
        
        # case "4":
        #     #удаление данных
        #     del_data()
            
        # case "5":
        #     #выход
        #     exit(0)
            
        # case _:
        #     print("неверный ввод")
        #     time.sleep(3)           
import sqlite3
import os
p = os.path.abspath("personal1.db")
print(p)
# import izmenenie (не обращайте внимания на эту строчку, дальше будет объянение(но это не точно))
db = sqlite3.connect("personal1.db")
cur = db.cursor()
# cur.execute('''CREATE TABLE sotrudniki (
#     id INTEGER PRIMARY KEY,
#     dolzhnost text NOT NULL,
#     fio text NOT NULL,
#     doki_id INTEGER NOT NULL,
#     log TEXT NOT NULL,
#     par TEXT NOT NULL,
#     FOREIGN KEY(doki_id) REFERENCES documents(id)
# )'''
# )

# cur.execute('''CREATE TABLE documents (
#     id INTEGER PRIMARY KEY,
#     passport INTEGER,
#     medknizhka INTEGER,
#     vaktsina INTEGER
# )''')


# cur.execute("SELECT * FROM sotrudniki")
# res = cur.fetchall()
# print(res)



def choices():
    print("Что делаем?")
    choice = int(input("Для входа выберите - 1   Для регистрациии выбирете - 2 "))
    if choice == 1:
       return checkdetails()
    elif choice == 2:
       return getdetails()
    else:
       raise TypeError


def checkdetails():
    db = sqlite3.connect("personal1.db")
    cur = db.cursor()
    login = input("Введите Lогин: ")
    cur.execute(f"SELECT log FROM sotrudniki WHERE log = '{login}'")
    if cur.fetchone() is None:
        print("Такой пользователь не найден. Пожалуйста, проверьте свой логин или зарегестрируйтесь")
    else:
        password = input("Введите пароль: ")
        cur.execute(f"SELECT par FROM sotrudniki WHERE par = '{password}'")
        if cur.fetchone() is None:
            print("Введеный пароль оказался неверным")
        else:
            print("Приветсвую вас, " + f"{login}" + " !")
            if login == "director":
                print("Вы вошли как директор. Разрешен доступ к расширенному функционалу. Если хотите начать работать с данными, пропишите - work. Если вы хотите просто посмотреть данные, то напишите - show ")
                rabota = input("Напишите команду: ")
                rabota.upper()
                if rabota == 'work':
                    return add()
                elif rabota == 'show':
                    cur.execute("SELECT * FROM sotrudniki")
                    ress = cur.fetchall()
                    print(ress)
                else:
                    print("Ввод оказался неверным. Пожалуйста, проверьте написание команды " + rabota)

                

            else:
                print("Вы вошли как обычный пользователь. Вы имеете право посмотреть свои личные данные. Для этого необходимо ввести 'Вывести мои данные' ")
                base = input("Введите команду: ")
                base.upper()
                if base == "Вывести мои данные":
                    cur.execute(f"SELECT * FROM sotrudniki, documents WHERE log = '{login}'")
                    res = cur.fetchone()
                    print(res)

                
def getdetails():
    print("Напишите")
    dolzhnost = input("Введите должность: ")
    fio = input("Ваши ФИО: ")
    doki_id = input("ID по документам. Если вам необходимо объяснение предназначения данной строки, введите 'пояснение'. Если вы имеете представление что это, то просто введите число(можно любое, оно все равно редактируется)")
    if doki_id == 'пояснение':
        print("Данный столбец занимает память. Потому что он является неотемлимой частью в БД. Его назначение заключается в том, чтобы сортировать правильно документы по персоналу и не путать ваши личные данные с другими. На этапе регистрации вы имеете право ввести любое число, так как после администратор его отредактирует на правильное.")
        doki_id = input("ID по документам. Если вам необходимо объяснение предназначения данной строки, введите 1. Если вы имеете представление что это, то просто введите число(можно любое, оно все равно редактируется)")
    log = input("Ваш будущий логин: ")
    par = input("Ваш будущий пароль: ")
    par2 = input("Подтвердите ваш будущий пароль: ")
    if par2 == par:
        cur.execute('INSERT INTO sotrudniki (dolzhnost, fio, doki_id, log, par) VALUES(?, ?, ?, ?, ?)', [dolzhnost, fio, doki_id, log, par])
        print("Вы были успешно зарегистрированы!")
    else:
        print("При подтверждении пароля произошла ошибка. Пожалуйста, повторите ввод")




def add():
    print("Здесь находится рабочая область для админов. Давайте приступим к работе. Что вы хотите сделать? (add - добавить данные, del1 - удалить сотрудника, del2 - удалить данные, edit - редактировать данные show1 - посомтреть данные, show2 - Личные данные сотрудника")
    bd = input("Введите действие: ")
    bd.upper()
    if bd == 'add':
        print("Что именно вы хотите добавить? Если нового сотрудника, напишите 1, если личные данные сотрудника, напишите 2")
        add_do = input("Введите: ")
        add_do.upper()
        if add_do == "1":
            dolzhnost = input("Введите должность: ")
            fio = input("ФИО: ")
            doki_id = input("ID по документам. Если вам необходимо объяснение предназначения данной строки, введите 'пояснение'. Если вы имеете представление что это, то просто введите число(можно любое, оно все равно редактируется)")
            if doki_id == 'пояснение':
                print("Данный столбец занимает память. Потому что он является неотемлимой частью в БД. Его назначение заключается в том, чтобы сортировать правильно документы по персоналу и не путать ваши личные данные с другими. На этапе регистрации вы имеете право ввести любое число, так как после администратор его отредактирует на правильное.")
                doki_id = input("ID по документам. Если вам необходимо объяснение предназначения данной строки, введите 1. Если вы имеете представление что это, то просто введите число(можно любое, оно все равно редактируется)")
            log = input("Логин: ")
            par = input("Пароль: ")
            par2 = input("Подтвердите пароль: ")
            if par2 == par:
                cur.execute('INSERT INTO sotrudniki (dolzhnost, fio, doki_id, log, par) VALUES(?, ?, ?, ?, ?)', [dolzhnost, fio, doki_id, log, par])
                print("Новый сотрудник успешно добавлен!")
                while True:
                    vernut = input("Хотите сделать что-то еще? да / нет: ")
                    if vernut == "да":
                        add()
                    else:
                        print("Работа с данными окончена!")
                        break
            else:
                print("При подтверждении пароля произошла ошибка. Пожалуйста, повторите ввод")
                while True:
                    vernut = input("Хотите продолжить работу? да / нет: ")
                    if vernut == "да":
                        add()
                    else:
                        print("")
                        break
                
        elif add_do == "2":
            idshnik = input("Введите id: ")
            passport = input("Введите паспортные данные: ")
            medkn = input("Введите данные мед.книжки: ")
            vaktsina = input("Введите данные о вакцинации: ")
            cur.execute(f'INSERT INTO documents (id, passport, medknizhka, vaktsina) VALUES(?, ?, ?, ?)', [idshnik, passport, medkn, vaktsina])
            print("Данные были успешно добавлены!")
            while True:
                vernut = input("Хотите сделать что-то еще? да / нет: ")
                if vernut == "да":
                    add()
                else:
                    print("Работа с данными закончена!")
                    break
    if bd == 'del1':
        dell = input("Данные под каким id вы хотите удалить?(Сам сотрудник) ")
        if dell == '1':
            print("Error")
            # return zahoteludalitadmina()
        else:
            cur.execute(f'DELETE FROM sotrudniki WHERE id = "{dell}"')
            print("Данные были успешно удалены!")
            while True:
                    vernut = input("Хотите сделать что-то еще? да / нет: ")
                    if vernut == "да":
                        add()
                    else:
                        print("Работа с данными закончена!")
                        break
    if bd == 'del2':
        dell = input("Данные под каким id вы хотите удалить?(Его документы) ")
        cur.execute(f'DELETE FROM documents WHERE id = "{dell}"')
        print("Данные были успешно удалены!")
        while True:
                    vernut = input("Хотите сделать что-то еще? да / нет: ")
                    if vernut == "да":
                        add()
                    else:
                        print("Работа с данными закончена!")
                        break
    if bd == 'show1':
        showw = input("Чьи данные вам необходимы? (id): ")
        cur.execute(f"SELECT * FROM sotrudniki WHERE id = {showw} ")
        result = cur.fetchall()
        print(result)
        while True:
                    vernut = input("Хотите сделать что-то еще? да / нет: ")
                    if vernut == "да":
                        add()
                    else:
                        print("Работа с данными закончена!")
                        break
    if bd == 'show2':
        showw = input("Чьи данные вам необходимы? (id): ")
        cur.execute(f"SELECT * FROM documents WHERE id = {showw} ")
        result = cur.fetchall()
        print(result)
        while True:
                    vernut = input("Хотите сделать что-то еще? да / нет: ")
                    if vernut == "да":
                        add()
                    else:
                        print("Работа с данными закончена!")
                        break
    if bd == 'edit':
        hui = input("Что именно вы хотите изменить? Ошибки в данных сотрудника - sr Ошибки в личных данных сотрудника - dc ")
        if hui == 'sr':
            a = input("Введите id сотрудника: ")
            b = input("Введите должность сотрудника(Если данный столбец остается неизменным, то просто введите старые данные сотрудника): ")
            c = input("Введите ФИО сотрудника(Если данный столбец остается неизменным, то просто введите старые данные сотрудника): ")
            d = input("Введите id сотрудника по его личным документам(Обычно, соответсвует id сотрудника): ")
            e = input("Введите логин сотрудника(Если данный столбец остается неизменным, то просто введите старые данные сотрудника): ")
            f = input("Введите пароль сотрудника(Если данный столбец остается неизменным, то просто введите старые данные сотрудника): ")
            # izmenenie.izm(a,b)
            cur.execute(f"UPDATE sotrudniki SET dolzhnost = '{b}' WHERE id = '{a}' ")
            cur.execute(f"UPDATE sotrudniki SET fio = '{c}' WHERE id = '{a}' ")
            cur.execute(f"UPDATE sotrudniki SET doki_id = '{d}' WHERE id = '{a}' ")
            cur.execute(f"UPDATE sotrudniki SET log = '{e}' WHERE id = '{a}' ")
            cur.execute(f"UPDATE sotrudniki SET par = '{f}'  WHERE id = '{a}' ")
            # cur.execute(f"SELECT * FROM sotrudniki id = {a} ")
            # print("Данные были изменены!")
            # resultat = cur.fetchone()
            # print(resultat)

            print("Данные были успешно обновлены!")
            while True:
                    vernut = input("Хотите сделать что-то еще? да / нет: ")
                    if vernut == "да":
                        add()
                    else:
                        print("Работа с данными закончена!")
                        break
        elif hui == 'dc':
            a2 = input("Введите id документов сотрудника : ")
            b2 = input("Введите паспортные данные сотрудника : ")
            c2 = input("Введите данные медкнижки сотрудника : ")
            d2= input("Введите данные о вакцинации сотрудника : ")
            cur.execute(f"UPDATE documents SET passport = '{b2}' WHERE id = '{a2}' ")
            cur.execute(f"UPDATE documents SET medknizhka = '{c2}' WHERE id = '{a2}' ")
            cur.execute(f"UPDATE documents SET vaktsina = '{d2}' WHERE id = '{a2}' ")
            print("Личные данные сотрудника были успешно изменены!")
            while True:
                    vernut = input("Хотите сделать что-то еще? да / нет: ")
                    if vernut == "да":
                        add()
                    else:
                        print("Работа с данными закончена!")
                        break

    


# def zahoteludalitadmina():
#     for i in range(9999):
#         print("Как вы посмели попытаться удалить самомо админа??? Теперь, пока не решите этот пример, вы не сможете выйти отсюда!!!")
#         print("1000 - 346 = ?")
#         otvet = input("введите ответ: ")
#         if otvet != 554:
#             print("Считай лучше!")
#         else:
#             print("Ладно, молодец, но запомни! Удалять админа нельзя!")
#             break

# def izm(a, b, c, d, e, f):
#     cur.execute(f"UPDATE sotrudniki SET dolzhnost = '{b}' WHERE id = '{a}'; ")
#     cur.execute(f"UPDATE sotrudniki SET fio = '{c}' WHERE id = '{a}'; ")
#     cur.execute(f"UPDATE sotrudniki SET doki_id = '{d}' WHERE id = '{a}'; ")
#     cur.execute(f"UPDATE sotrudniki SET log = '{e}' WHERE id = '{a}'; ")
#     cur.execute(f"UPDATE sotrudniki SET par = '{f}'  WHERE id = '{a}'; ")
#     cur.execute(f"SELECT * FROM sotrudniki id = {a} ")
#     print("Данные были изменены!")
#     db.commit()
    


print(choices())



db.commit()
db.close()

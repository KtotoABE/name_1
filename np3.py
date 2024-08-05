import pandas as pd
import os
import sqlite3 as sl
import sqlite3 as sq
import sqlite3
from contextlib import closing
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Пользователи (
ID INTEGER PRIMARY KEY,
name TEXT NOT NULL,
mail TEXT NOT NULL,
age INTEGER
)
''')
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()
cursor.execute('SELECT * FROM Пользователи')
Пользователи = cursor.fetchall()
for name in Пользователи:
    print(name)
print('1)добавить пользовотеля ')
print('2)удалить пользовотеля ')
print('3)изменить пользовотеля ')
print('0)выход ')
a = int(input('введите значение от 0 до 3   '))
match a:
    case 0:
        connection.commit()
        connection.close()
        print("Вы успешно вышли")
    case 1:
        name1 = input("Введите ваше имя: ")
        mail1 = input("Введите вашу почту: ")
        age1 = input("Введите ваш возраст: ")
        cursor.execute('INSERT INTO Пользователи (name, mail, age) VALUES (?, ?, ?)', (name1, mail1, age1))
        connection.commit()
        connection.close()
        print("Пользователь успешно добавлен")
    case 2:
        id = input("Введите id человека для удаления: ")
        cursor.execute("DELETE FROM Пользователи WHERE ID = ?",(id,))
        connection.commit()
        connection.close()
        print("Пользователь успешно удалён")
    case 3:
        input_new = input('Имя ользователя для изменения ')
        input_change = input('Заменить имя на - ')
        sql = "UPDATE Пользователи SET name = ?" "WHERE name = ?"
        cursor.execute(sql, [input_change, input_new])
        connection.commit()
        connection.close()
        print("Имя успешно изменено")
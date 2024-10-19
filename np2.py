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
a= int(input('введите значение от 1 до 3   '))
print(a)
if a == 0:
    connection.commit()
    connection.close()
elif a == 1:
    name1 = input("Введите ваше имя: ")
    mail1 = input("Введите вашу почту: ")
    age1 = input("Введите ваш возраст: ")
    cursor.execute('INSERT INTO Пользователи (name, mail, age) VALUES (?, ?, ?)', (name1, mail1, age1))
    connection.commit()
    connection.close()
if a == 2:
    id = input("Введите id человека для удаления: ")
    cursor.execute("DELETE FROM Пользователи WHERE ID = ?",(id,))
    connection.commit()
    connection.close()
elif a == 3:
    id = input("Введите идентификатор записи для обновления: ")
    new_value = input("Введите новое значение: ")
    cursor.execute("UPDATE Пользователи SET ID = ? WHERE id = ?", (new_value, id))
    connection.commit()
    connection.close()
else: a == 21311331131313313113311234213421341234124123412341241234123341234123412412334123413243124132414
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()
cursor.execute('SELECT * FROM Пользователи')
Пользователи = cursor.fetchall()
for name in Пользователи:
    print(name)
connection.close()
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()
connection.commit()
connection.close()
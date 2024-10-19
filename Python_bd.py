import sqlite3
from datetime import datetime
import re

def is_valid_email(email):
    return re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email) is not None

def is_valid_date(date_string):
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False
connection = sqlite3.connect('users_database.db')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    email TEXT NOT NULL,
    absence_date DATE DEFAULT '',
    work_date DATE DEFAULT '',
    registration_date DATE NOT NULL
)
''')

def add_user():
    full_name = input("Enter full name: ")
    email = input("Enter email address: ")
    if not is_valid_email(email): return print("Invalid email format.")
    registration_date = datetime.now().strftime("%Y-%m-%d")
    cursor.execute('INSERT INTO users (full_name, email, registration_date) VALUES (?, ?, ?)',
                   (full_name, email, registration_date))
    connection.commit()
    print("User successfully added.")

def update_user():
    user_id = input("Enter user ID or full name to update: ")
    column = input("Which column to update (full_name/email)? ")
    new_value = input("Enter new value: ")
    if column == "email" and not is_valid_email(new_value):
        return print("Invalid email format.")
    cursor.execute(f"UPDATE users SET {column} = ? WHERE id = ? OR full_name = ?",
                   (new_value, user_id, user_id))
    connection.commit()
    print("User information successfully updated.")

def add_absence_date():
    user_id = input("Enter user ID or full name to add absence date: ")
    absence_date_input = input("Enter absence date (YYYY-MM-DD) or leave empty for today: ")
    absence_date_input = absence_date_input or datetime.now().strftime("%Y-%m-%d")
    if not is_valid_date(absence_date_input): return print("Invalid date format.")
    if datetime.strptime(absence_date_input, "%Y-%m-%d") < datetime.now():
        return print("Absence date cannot be earlier than the current date.")
    cursor.execute("UPDATE users SET absence_date = ? WHERE id = ? OR full_name = ?",
                   (absence_date_input, user_id, user_id))
    connection.commit()
    print("Absence date successfully added.")

def add_work_date():
    user_id = input("Enter user ID or full name to add work date: ")
    work_date_input = input("Enter work date (YYYY-MM-DD): ")
    if not is_valid_date(work_date_input): return print("Invalid date format.")
    cursor.execute("UPDATE users SET work_date = ? WHERE id = ? OR full_name = ?",
                   (work_date_input, user_id, user_id))
    connection.commit()
    print("Work date successfully added.")

def delete_user():
    user_id_or_name = input("Enter user ID or full name to delete: ")
    cursor.execute("DELETE FROM users WHERE id = ? OR full_name = ?", (user_id_or_name, user_id_or_name))
    connection.commit()
    print("User successfully deleted.")

menu_options = {
    1: add_user,
    2: update_user,
    3: add_absence_date,
    4: add_work_date,
    5: delete_user,
}

while True:
    print("\nMenu:\n1) Add user\n2) Update user\n3) Add absence date\n4) Add work date\n5) Delete user\n0) Exit")
    choice = int(input("Select an option: "))
    if choice == 0: break
    if choice in menu_options:
        menu_options[choice]()
    else:
        print("Invalid option. Please try again.")

connection.close()
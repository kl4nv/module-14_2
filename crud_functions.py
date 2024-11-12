import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INT,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL)
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL)
    ''')


def get_all_products():
    cursor.execute('SELECT * FROM Products')
    return cursor.fetchall()


def add_user(username, email, age):
    cursor.execute('INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)',
                   (username, email, age, 1000))
    connection.commit()


def is_included(username):
    if cursor.execute('SELECT username FROM Users WHERE username = ?', (username, )).fetchone():
        return True
    else:
        return False



initiate_db()

if len(get_all_products()) == 0:
    for i in range(1, 5):
        cursor.execute('INSERT INTO Products(id, title, description, price) VALUES(?, ?, ?, ?)',
                       (i, f'Витамин {i}', f'Описание {i}', i * 1000))

connection.commit()


if __name__ == "__main__":
    connection.close()

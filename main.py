# import socket
# import view import index, blog

# URLS = {

#     '/': index,
#     '/blog': blog

# }

# def parse_request(request):
#     parsed = request.split()
#     method = parsed[0]
#     url = parsed[1]
#     return method, url

# def generate_headers(method, url):
#     if method != 'GET':
#         return 'HTTP/1.1 405 Method Not Allowed!\n\n', 405
#     if url not in URLS:
#         return 'HTTP/1.1 404 Page Not Found!\n\n', 404
#     return 'HTTP/1.1 200 OK!\n\n', 200

# def generate_content(code, url):
#     if code == 404:
#         return '<h1>404</h1><h3>Page Not Found!</h3>'
#     elif code == 405:
#         return '<h1>404</h1><h3>Method Not Allowed!</h3>'
#     return URLS[url]()


# def generate_response(request):
#     method, url = parse_request(request)
#     headers, code = generate_headers(method, url)
#     body = generate_content(code, url)
#     return (headers + body).encode()

# def run():
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.bind(('127.0.0.1', 5000))
#     server_socket.listen()

#     while True:
#         client_socket, addr = server_socket.accept()
#         request = client_socket.recv(1024)
#         print(f"Клиент: {addr} => \n{request.decode('utf-8')}\n")
#         response = generate_response(request.decode())
#         client_socket.sendall(response)
#         client_socket.close()



# if __name__ == "__main":
#     run()
# con = sqlite3.connect("profile.db")
# cur = con.cursor()

# cur.execute("""
# """)

# con.close()

# cur.execute(CREATE TABLE IF NOT EXISTS users(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         summa REAL,
#         date TEXT
#     ))

# with sqlite3.connect("profile.db") as con:
#     cur = con.cursor()
#     # cur.execute("""CREATE TABLE IF NOT EXISTS users(
#     # id INTEGER PRIMARY KEY AUTOINCREMENT,
#     # name TEXT NOT NULL,
#     # summa REAL,
#     # date TEXT
#     # )""")
#     cur.execute("DROP TABLE users")
    
# with sqlite3.connect("users.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     DROP TABLE person_table           
#     """)
    
    # cur.execute("""
    # ALTER TABLE person_table
    # DROP COLUMN address            
    # """)
    
    
    # cur.execute("""
    # ALTER TABLE person
    # RENAME TO person_table;            
    # """)
    
    
    # cur.execute("""CREATE TABLE IF NOT EXISTS person(
    # id INTEGER PRIMARY KEY AUTOINCREMENT,
    # name TEXT NOT NULL,
    # phone BLOB NOT NULL DEFAULT  "+79004005060",
    # age INTEGER CHECK (age > 0 AND age < 100),
    # email TEXT UNIQUE
    # )""")
    
# with sqlite3.connect("db_3.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#         SELECT *
#         FROM T1
#         LIMIT 5 OFFSET 2
#     """)
    
#     res = cur.fetchall()
#     print(res)
#     res2 = cur.fetchmany()
#     print(res2)
    
    # for i in cur:
    #     print(i)
    
# with sqlite3.connect("education.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS student(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         surname TEXT NOT NULL,
#         name TEXT NOT NULL,
#         patronymic TEXT NOT NULL,
#         age INTEGER NOT NULL CHECK (age >= 16 AND age <= 45),
#         [group] TEXT NOT NULL,
#         FOREIGN KEY ([group]) REFERENCES groups (id) ON DELETE RESTRICT
#     )""")
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS groups(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         group_name TEXT NOT NULL
#     )""")
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS lessons(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         lesson_title TEXT NOT NULL
#     )""")
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS association(
#         lesson_id INTEGER NOT NULL,
#         group_id INTEGER NOT NULL,
#         FOREIGN KEY (group_id) REFERENCES groups (id)
#         FOREIGN KEY (lesson_id) REFERENCES lessons (id)
#     )""")

# with sqlite3.connect("study.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS students(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         surname TEXT NOT NULL,
#         name TEXT NOT NULL,
#         age INTEGER NOT NULL CHECK (age >= 16 AND age <= 45),
#         [course] TEXT NOT NULL,
#         FOREIGN KEY ([course]) REFERENCES courses (id) ON DELETE RESTRICT
#     )""")
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS courses(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         course_name TEXT NOT NULL
#     )""")
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS registration(
#         student_id INTEGER NOT NULL,
#         course_id INTEGER NOT NULL,
#         FOREIGN KEY (student_id) REFERENCES students (id)
#         FOREIGN KEY (course_id) REFERENCES courses (id)
#     )""")


# cars = [
#     ('BMW', 54000),
#     ('Chevrolet', 34000),
#     ('Ferarri', 74000),
#     ('Citroen', 24000),
#     ('Honda', 33000),
# ]

# with sqlite3.connect("cars.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS car(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         prise INTEGER
#     ) 
#     """)
    
#     cur.executescript("""
#     DELETE FROM car WHERE model LIKE 'B%';
#     UPDATE car SET prise = prise + 111;    
                      
#     """)
    
    #cur.execute("UPDATE car SET prise = :Prise WHERE model LIKE 'B%'", {'Prise':0})
    
    #cur.executemany("INSERT INTO car VALUES(NULL, ?, ?)", cars)
    
    # for car in cars:
    #     cur.execute("INSERT INTO car VALUES(NULL, ?, ?)", car)
        
    
    # cur.execute("INSERT INTO car VALUES(1, 'Renault', 22000)")
    # cur.execute("INSERT INTO car VALUES(2, 'Volvo', 22000)")
    # cur.execute("INSERT INTO car VALUES(3, 'Mercedes', 20000)")
    # cur.execute("INSERT INTO car VALUES(4, 'Bentley', 32000)")
    # cur.execute("INSERT INTO car VALUES(5, 'Audi', 22000)")
# con = None
# try:
#     con = sqlite3.connect("cars.db")
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS car(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         prise INTEGER
#     );
#     BEGIN;
#     INSERT INTO car VALUES(NULL, 'Renault', 22000);
#     UPDATE car SET prise = prise + 111;
#     """)
#     con.commit()

# except sqlite3.Error as e:
#     if con:
#         con.rollback()
#     print("Ошибка выполнения запроса", e)
# finally:
#     if con:
#         con.close()

# CREATE TABLE IF NOT EXISTS cost(
    #     name TEXT, tr_in INTEGER, buy INTEGER
    # )
    # """)
    
    # cur.execute("SELECT model, prise FROM car")
    # for res in car:
    #     print(res)
    # # row = cur.fetchone()
    # # print(row)
    # # row2 = cur.fetchmany(5)
    # # print(row2)
    # # row3 = cur.fetchmany(5)
    # # print(row3)
    
    # # cur.execute("INSERT INTO car VALUES(NULL, 'Запорожец', 1000)")
    # # last_row_id = cur.lastrowid
    # # buy_car_id = 2
    # # cur.execute("INSERT INTO cost VALUES('Илья', ?, ?)", (last_row_id, buy_car_id))

# def read_ava(n):
#     try:
#         with open(f"avatars/{n}.png", "rb") as f:
#             return f.read()
#     except IDError as e:
#         print(e)
#         return False
#     return True

# def write_ava(name, data):
#     try:
#         with open(name, "wb") as f:
#             f.write(data)
#     except IDError as e:
#         print(e)
#         return 

# with sqlite3.connect("cars.db") as con:
#     con.row_factory = sqlite3.Row
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS users(
#         name TEXT,
#         ava BLOB,
#         score INTEGER
#     );
#     """)


# cur.execute("SELECT ava FROM users")
# img = cur.fetchone()['ava']
# write_ava("out.png", img)
    
# img = read_ava(1)
# if img:
#     binary = sqlite3.Binary(img)
#     cur.execute("INSERT INTO users VALUES('Илья', ?, 1000)", (binary,))
        
import sqlite3
# with sqlite3.connect("cars.db") as con:
#     cur = con.cursor()
    
#     with open("sql_dump.sql", "w") as f:
#         for sql in con.iterdump():
#             f.write(sql)
# with sqlite3.connect("cars.db") as con:
#     cur = con.cursor()
    
#     with open("sql_dump.sql", "r") as f:
#         sql = f.read()
#         cur.executescript(sql)

# ************************************
# import sqlalchemy as db
#
# engine = db.create_engine('sqlite:///products-sqlalchemy.db')
#
# connection = engine.connect()
#
# metadata = db.MetaData()
#
# products = db.Table('Products', metadata,
#                     db.Column('product_id', db.Integer, primary_key=True),
#                     db.Column('product_name', db.Text),
#                     db.Column('supplier_name', db.Text),
#                     db.Column('price_per_tonne', db.Integer)
# )
#
# metadata.create_all(engine)
#
# insertion_query = products.insert().values([
#     {"product_name":"Banana", "supplier_name":"United Bananas", "price_per_tonne":7000},
#     {"product_name":"Avocado", "supplier_name":"United Avocados", "price_per_tonne":12000},
#     {"product_name":"Tomatoes", "supplier_name":"United Tomatoes", "price_per_tonne":3000}
# ])

# connection.execute(insertion_query)
# select_all_query = db.select([products])
# select_all_result = connection.execute(select_all_query)
#
# print(select_all_result.fetchall())
# ************************************

# ORM
# pip install sqlalchemy
# pip install faker
#
# import os
# from models.database import create_db, Session
# from models.lesson import Lesson
# from models.student import Student
# from models.group import Group
# from models.database import DATABASE_NAME
# import create_database as db_creator
# from models.database import Base
# from sqlalchemy import Column, Integer, String, ForeignKey, Table
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
#
# if __name__ == '__main__':
#     db_is_created = os.path.exists(DATABASE_NAME)
#     if not db_is_created:
#         db_creator.create_database()
#
#
# for it in session.query(Student.age):
#     print(it)
# print("*" * 60)

from jinja2 import Template

# name = "Igor"
# age = 29
# per = {'name': "Igor", 'age': 28}

# class Person:
#     def __int__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_name(self):
#         return self.name
#
# per = Person("Igor",29)

# teg = [
#     {'href': 'index', 'title': 'Главная'},
#     {'href': 'news', 'title': 'Новости'},
#     {'href': 'about', 'title': 'О компании'},
#     {'href': 'shop', 'title': 'Магазин'},
#     {'href': 'contacts', 'title': 'Контакты'},
# ]
#
# link = '''<ul>
# {% for t in teg -%}
# {% if t.title == 'Главная' -%}
#     <li><a href="/{{ t['href'] }}" class="active">{{ t['title'] }}</a></li>
# {% else -%}
#     <li><a href="/{{ t['href'] }}">{{ t['title'] }}</a></li>
# {% endif -%}
# {% endfor -%}
# </ul>'''
#
# tm = Template(link)
# msg = tm.render(teg=teg)
# print(msg)

# cars = [
#     {'model': 'Audi', 'price': 23000},
#     {'model': 'Skoda', 'price': 17300},
#     {'model': 'Renault', 'price': 44300},
#     {'model': 'Wolksvagen', 'price': 21300}
# ]
#
# # tpl = "{{ cs | sum(attribute='price') }}"
# # tpl = "{{ cs | max(attribute='price') }}"
# # tpl = "{{ (cs | min(attribute='price')).model }}"
# # tpl = "{{ cs | random }}"
# tpl = "{{ cs | replace('model', 'brand') }}"
#
# tm = Template(tpl)
# msg = tm.render(cs=cars)
# print(msg)

# Макроопределения

html = """
{%macro set_input(name, placeholder='', type='text')-%}
    <input type="{{type}}" name="{{name}}" placeholder="{{placeholder}}">
{%endmacro-%}

<p>{{set_input('firstname', placeholder='Имя')}}</p>
<p>{{set_input('lastname', placeholder='Фамилия')}}</p>
<p>{{set_input('address', placeholder='Адрес')}}</p>
<p>{{set_input('phone', type='tel', placeholder='Телефон')}}</p>
<p>{{set_input('email', type='email', placeholder='Почта')}}</p>
"""

tm = Template(html)
msg = tm.render()
print(msg)


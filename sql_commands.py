

from config import *
import psycopg2
from psycopg2 import Error


def start_base():
    global conn
    try:
        conn = psycopg2.connect(database=database,
                                user=user,
                                password=password,
                                port=port,
                                host=host)
        print('Успешное подключение к БД!')
    except (Exception, Error) as e:
        print('Ошибка подключения к PostgreSQL')
        print(e)


def register_user(uid):
    with conn:
        with conn.cursor() as curs:
            curs.execute("INSERT INTO users VALUES (%s) ;", (uid,))


def record_user(name, date, time):
    with conn:
        with conn.cursor() as curs:
            curs.execute("INSERT INTO records VALUES (%s, %s, %s) ;", (name, date, time,))

def check_record(date, time):
    with conn:
        with conn.cursor() as curs:
            curs.execute("select name, date, time from records where date = %s and time = %s;", (date, time,))
            if curs.fetchone():
                return True

def show_empty_slots():
    with conn:
        with conn.cursor() as curs:
            curs.execute("select * from records where name = '';",)
            return curs.fetchall()




# def test_input_table():
#     try:
#         conn = psycopg2.connect(database=database,
#                                 user=user,
#                                 password=password,
#                                 port=port,
#                                 host=host)
#         print('Успешное подключение к БД!')
#     except (Exception, Error) as e:
#         print('Ошибка подключения к PostgreSQL')
#         print(e)
#
#     curs = conn.cursor()
#
#     my_type = ['9:00-9:30', '9:30-10:00', '10:00-10:30', '10:30-11:00']
#
#     today = datetime.date(2023, 5, 15)
#     day = 1
#     while day != 4:
#         next_day = today + datetime.timedelta(days=day)
#         day += 1
#         for i in range(len(my_type)):
#             print(next_day, my_type[i])
#             curs.execute("INSERT INTO records (name, date, time) VALUES (%s, %s, %s);", ('', next_day, my_type[i],))
#
#     curs.close()
#     conn.commit()
# select * from records where date = '2023-05-26' order by time;
# select * from records where date between '2023-05-20' and '2023-05-26' and name = '';
# update records set name = 'Viktor' where date = '2023-05-26' and time = '10:00-10:30';
# test_input_table()

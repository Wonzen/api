import psycopg2
from psycopg2 import Error

try:
    # Подключиться к существующей базе данных
    connection = psycopg2.connect(user="postgres",
                                  # пароль, который указали при установке PostgreSQL
                                  password="VbrrbVf",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="addressbook")

    cursor = connection.cursor()
    postgresql_select_query = "select * from users"
    cursor.execute(postgresql_select_query)
    table_users = cursor.fetchall()

    print ("Вывод записей", table_users)

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")
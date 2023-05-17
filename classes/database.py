import pymysql
from config import *

class DB:
    def __init__(self):
        self.connection = pymysql.connect( #кортеж, неизменяемый список
            host = host,
            port = port,
            user = user,
            password = password,
            database = database
        )

    def add_user(self, login, password, name, surname): #добавление пользователя

        with self.connection.cursor() as cursor:
            insert_query = f"INSERT INTO user (login, password, name, surname) VALUES (%s, %s, %s, %s);"
            cursor.execute(insert_query, [login, password, name, surname]) #выполнение запроса
            self.connection.commit() #сохранение изменения в базе данных
    
    def delete_user(self, login): #удаление пользователя по логину

        with self.connection.cursor() as cursor:
            delete_query = f"DELETE FROM user WHERE login = %s;"
            cursor.execute(delete_query, [login])
            self.connection.commit()

    def authorized_user(self, login, password): #авторизован пользователь или нет

        with self.connection.cursor() as cursor:
            select_query = f"SELECT * FROM user WHERE login = %s and password = %s;"
            flag = cursor.execute(select_query, [login, password])

        return flag
        
    def __del__(self):
        self.connection.close()

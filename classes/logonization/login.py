from tkinter import *
from tkinter import messagebox

root = Tk() #основа

root.title('Login') #название
root.geometry('925x500+300+200') #размер
root.configure(bg = 'white') #цвет заднего фона
root.resizable(False, False) #неизменный экран


img = PhotoImage(file = 'image\login.png') #изображение 
Label(root, image = img, bg = 'white').place(x = 50, y = 50)  #расположение изображения

frame = Frame(root, width = 350, height = 350, bg = 'white') #создание основного фрейма
frame.place(x = 480, y = 70) #расположение фрейма

heading = Label(frame, text = 'Авторизация', fg = '#57a1f8', bg = 'white', font = ('Microsoft YaHei UI Light', 23, 'bold')) #оформление заголовка
heading.place(x = 76, y = 5) #расположение заголовка

##########################
#видно, не видно
def on_enter(n): 
    user_in.delete(0, 'end')

def on_leave(n):
    name = user_in.get()
    if name == '':
        user_in.insert(0, 'username')

user_in = Entry(frame, width = 25, fg = 'grey', border = 0, bg = 'white', font = ('Microsoft YaHei UI Light', 11)) #оформление коробки логина
user_in.place(x = 30, y = 80) #расположение логина
user_in.insert(0, 'username') #внутри коробки логина
#видно, не видно
user_in.bind('<FocusIn>', on_enter) 
user_in.bind('<FocusOut>', on_leave)
Frame(frame, width = 295, height = 2, bg = 'light grey').place(x = 25, y = 107) #окончание блока логина
##########################

##########################
#видно, не видно
def on_enter(n): 
    password_in.delete(0, 'end')

def on_leave(n):
    password = password_in.get()
    if password == '':
        password_in.insert(0, 'password')

password_in = Entry(frame, width = 25, fg = 'grey', border = 0, bg = 'white', font = ('Microsoft YaHei UI Light', 11)) #оформление коробки пароля
password_in.place(x = 30, y = 150) #расположение пароля
password_in.insert(0, 'password') #внутри коробки пароля
#видно, не видно
password_in.bind('<FocusIn>', on_enter) 
password_in.bind('<FocusOut>', on_leave)
Frame(frame, width = 295, height = 2, bg = 'light grey').place(x = 25, y = 177) #окончание блока пароля
##########################

Button(frame, width = 39, pady = 9, text= 'войти', bg = '#57a1f8', fg = 'white', border = 0).place(x = 35, y = 204) #расположение войти

label = Label(frame, text = "Нет аккаунта?", bg = 'white', fg = 'black',  font = ('Microsoft YaHei UI Light', 9))
label.place(x = 76, y = 270) #расположение нет аккаунта

sign_up = Button(frame, width = 16, text = 'Зарегистрироваться', border = 0, bg = 'white', fg =  '#57a1f8', cursor = 'hand2')
sign_up.place(x = 157, y = 270) #расположение зарегистрироваться


root.mainloop() #запуск окна



from tkinter import *
from tkinter import messagebox
import ast #для обработки синтаксиса

root = Tk() #основа

root.title('Sign up') #название
root.geometry('925x500+300+200') #размер
root.configure(bg = 'white') #цвет заднего фона
root.resizable(False, False) #неизменный экран

img = PhotoImage(file = 'image\signup.png') #изображение 
Label(root, image = img, bg = 'white').place(x = 40, y = 40)  #расположение изображения

frame = Frame(root, width = 350, height = 400, bg = 'white') #создание основного фрейма
frame.place(x = 480, y = 70) #расположение фрейма

heading = Label(frame, text = 'Регистрация', fg = '#4F2982', bg = 'white', font = ('Bitter', 23, 'bold')) #оформление заголовка
heading.place(x = 76, y = 3) #расположение заголовка

##########################
#видно, не видно
def on_enter(n): 
    user_in.delete(0, 'end')

def on_leave(n):
    name = user_in.get()
    if name == '':
        user_in.insert(0, 'username')

user_in = Entry(frame, width = 25, fg = 'grey', border = 0, bg = 'white', font = ('Bitter', 11)) #оформление коробки логина
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

password_in = Entry(frame, width = 25, fg = 'grey', border = 0, bg = 'white', font = ('Bitter', 11)) #оформление коробки пароля
password_in.place(x = 30, y = 150) #расположение пароля
password_in.insert(0, 'password') #внутри коробки пароля
#видно, не видно
password_in.bind('<FocusIn>', on_enter) 
password_in.bind('<FocusOut>', on_leave)
Frame(frame, width = 295, height = 2, bg = 'light grey').place(x = 25, y = 177) #окончание блока пароля
##########################

##########################
#видно, не видно
def on_enter(n): 
    password_in_repeat.delete(0, 'end')

def on_leave(n):
    repeat_password = password_in_repeat.get()
    if repeat_password == '':
        password_in_repeat.insert(0, 'repeat password')

password_in_repeat = Entry(frame, width = 25, fg = 'grey', border = 0, bg = 'white', font = ('Bitter', 11)) #оформление коробки пароля
password_in_repeat.place(x = 30, y = 220) #расположение пароля
password_in_repeat.insert(0, 'repeat password') #внутри коробки пароля
#видно, не видно
password_in_repeat.bind('<FocusIn>', on_enter) 
password_in_repeat.bind('<FocusOut>', on_leave)
Frame(frame, width = 295, height = 2, bg = 'light grey').place(x = 25, y = 247) #окончание блока пароля
##########################

Button(frame, width = 39, pady = 9, text= 'Зарегистрироваться', bg = '#530FAD', fg = 'white', font = ('Bitter', 9), border = 0).place(x = 35, y = 274) #расположение зарегистрироваться

label = Label(frame, text = "У меня уже есть аккаунт", bg = 'white', fg = 'black',  font = ('Bitter', 9))
label.place(x = 76, y = 340) #расположение есть аккаунт

sign_up = Button(frame, width = 4, text = 'Войти', border = 0, bg = 'white', fg =  '#530FAD', font = ('Bitter', 9), cursor = 'hand2')
sign_up.place(x = 223, y = 340) #расположение зарегистрироваться

root.mainloop()
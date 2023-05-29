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

heading = Label(frame, text = 'Sign in', fg = '#57a1f8', bg = 'white', font = ('Microsoft YaHei UI Light', 23, 'bold')) #оформление заголовка
heading.place(x = 120, y = 5) #расположение заголовка

user_in = Entry(frame, width = 25, fg = 'grey', border = 0, bg = 'white', font = ('Microsoft YaHei UI Light', 11)) #оформление коробки логина
user_in.place(x = 30, y = 80) #расположение логина
user_in.insert(0, 'username') #внутри коробки логина
Frame(frame, width = 295, height = 2, bg = 'light grey').place(x = 25, y = 107) #окончание блока логина

password_in = Entry(frame, width = 25, fg = 'grey', border = 0, bg = 'white', font = ('Microsoft YaHei UI Light', 11)) #оформление коробки пароля
password_in.place(x = 30, y = 150) #расположение пароля
password_in.insert(0, 'password') #внутри коробки пароля
Frame(frame, width = 295, height = 2, bg = 'light grey').place(x = 25, y = 177) #окончание блока пароля


root.mainloop() #запуск окна



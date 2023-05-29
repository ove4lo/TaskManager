from tkinter import *
from tkinter import messagebox

root = Tk() #основа

root.title('Login') #название
root.geometry('925x500+300+200') #размер
root.configure(bg = "#fff") #цвет заднего фона
root.resizable(False, False) #неизменный экран


img = PhotoImage(file = 'image\login.png') #изображение 
Label(root, image = img, bg = "#fff").place(x = 50, y = 50) 

root.mainloop() #запуск окна



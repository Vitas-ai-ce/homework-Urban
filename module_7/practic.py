import tkinter
import os
from tkinter import filedialog
from tkinter import Menu
from tkinter import messagebox

# Функции для обработки команд
def file_select():
    filename = filedialog.askopenfilename(initialdir= '/', title= 'Выберите файл',
                                          filetypes= (('Текстовый файл', '.txt'),
                                                      ('Все файлы', '*')))
    text['text'] = text['text'] + '' + filename
    os.startfile(filename)
def info():
    messagebox.showinfo("Новый файл", "Для работы используйте меню 'Файл' для открытия и сохранения документов,"
                                      " а текст можно редактировать в главном окне.")
def open_file():
    messagebox.showinfo("Открыть файл",  "Открытие файла")
def about():
    messagebox.showinfo("О программе", "Автор: В.Ильин, Версия: 1.0")


# Создание основного окна
window = tkinter.Tk()
window.title('Проводник')
window.geometry('600x150')
window.configure(bg='black')
window.resizable(False, False)
text = tkinter.Label(window, text='Файл:', height=5, width=70, background='silver',
                     foreground= 'blue')
text.grid(column=1, row=1)
button_select=tkinter.Button(window, width=67, height=3, text='Выбрать файл', background='silver',
                     foreground= 'blue', command= file_select)
button_select.grid(column=1, row=2)

# Создание главного меню
menu_bar = tkinter.Menu()

# Меню «Файл»
file_menu = tkinter.Menu(menu_bar, tearoff=0)
# Создаём подменю
file_menu.add_command(label="Новый", command=info, )  # Пункт «Новый»
file_menu.add_command(label="Открыть", command=open_file)  # Пункт «Открыть»
file_menu.add_separator()  # Разделитель
file_menu.add_command(label="Выход", command=window.quit)  # Пункт «Выход»
menu_bar.add_cascade(label ="Файл", menu=file_menu)  # Добавляем подменю «Файл» в главное меню

# Меню «Справка»
help_menu = tkinter.Menu(menu_bar, tearoff=0)

# Создаём подменю
help_menu.add_command(label="О программе", command=about)  # Пункт «О программе»
menu_bar.add_cascade(label="Справка", menu=help_menu)  # Добавляем подменю «Справка» в главное меню

# Привязка меню к окну
window.config(menu=menu_bar)
window.mainloop()

import tkinter.messagebox
from tkinter import *
import random
import string
import pygame


def motion():  # Циклическая анимация
    canv.move(bullet, 90, 30)
    if canv.coords(bullet)[2] < 1280:
        window.after(100, motion)
    else:
        canv.move(bullet, -450, -150)
        window.after(100, motion())


def shift(st, n, back_or_forward):  # Алгоритм сдвига символов
    symbols = string.ascii_uppercase + string.digits  # 36 символов в сумме
    if back_or_forward == 1:
        for i in range(len(st)):
            if symbols.index(st[i]) + n < 36:
                st = st.replace(st[i], symbols[symbols.index(st[i]) + n])
            else:
                st = st.replace(st[i], symbols[symbols.index(st[i]) + n - 36])
    else:
        for i in range(len(st)):
            st = st.replace(st[i], symbols[symbols.index(st[i]) - n])
    return st


def generate():  # Генерация кода и его размещение в окне
    num = num_entry.get()
    if num.isdigit():
        if len(num) == 3:
            code_parts = [''.join(random.choices(string.ascii_uppercase + string.digits, k=5))]
            code_parts.append(shift(code_parts[0][0:4], int(num[0]), 1))
            code_parts.append(shift(code_parts[1][0:3], int(num[1]), 2))
            code_parts.append(shift(code_parts[2][0:2], int(num[2]), 1))
            code = code_parts[0] + '-' + code_parts[1] + '-' + code_parts[2] + '-' + code_parts[3]
            canv.create_rectangle(600, 350, 1250, 425, fill='white', outline='black')
            canv.create_text(925, 350, anchor='n', text=code,  font='Calibri 44')
        else:
            err = 'Введено не трёхзначное число((((('
            tkinter.messagebox.showerror('Ошибка', err)
    else:
        err = 'Введено не число((((((('
        tkinter.messagebox.showerror('Ошибка', err)


pygame.mixer.init()
pygame.mixer.music.load('music.mp3')  # Воспроизведение прекрасной музыки
pygame.mixer.music.play(loops=99)

window = Tk()

bg = PhotoImage(file='bg.png')  # загружаем фото

window.geometry('1280x1024')
canv = Canvas(window, height=1280, width=1024)  # настраиваем окно
canv.pack(fill='both', expand=1)

canv.create_image(640, 512, image=bg)  # добавляем фон

canv.create_text(
    640, 50,
    text='Генератор кодов на гаусс-пушку в S.T.A.L.K.E.R. Тень ванючки',
    fill='white',
    font='Calibri 32')

canv.create_rectangle(600, 250, 900, 325, fill='white', outline='black')
num_entry = Entry(window, width=300, font='Calibri 32')                  # окно ввода трёхзначного числа
num_entry.place(x=600, y=250, anchor='nw', height=75, width=300)

gen_button = Button(height=75, width=300, command=generate,
                    text='Сгенерировать код!', font='Calibri 24')  # кнопка для генерации кода
gen_button.place(x=950, y=250, height=75, width=300)

bullet = canv.create_line(960, 700, 1020, 720, width=10, fill='yellow')  # создаём объект анимации и анимируем
motion()

mainloop()

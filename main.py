from tkinter import *


def generate():
    print('')


window = Tk()
bg = PhotoImage(file='bg.png')
window.geometry('1280x1024')
canv = Canvas(window, height=1280, width=1024)
canv.pack(fill='both', expand=1)
canv.create_image(640, 512, image=bg)
canv.create_text(640, 50,
                 text='Генератор кодов на гаусс-пушку в S.T.A.L.K.E.R. Тень ванючки',
                 fill='white',
                 font='Calibri 32')
canv.create_rectangle(600, 250, 900, 325, fill='white', outline='black')
num = Entry(window, width=300, font='Calibri 32')
num.place(x=600, y=250, anchor='nw', height=75, width=300)
gen_button = Button(height=75, width=300, command=generate,
                    text='Сгенерировать код!', font='Calibri 24')
gen_button.place(x=950, y=250, height=75, width=300)
mainloop()

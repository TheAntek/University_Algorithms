from tkinter import *
import math


def window1(event):
    def result_1(event1):
        """Алгоритм 1"""
        user_1 = entry1.get()
        user_2 = entry2.get()
        user_3 = entry3.get()
        user_4 = entry4.get()
        try:
            a = float(user_1)
            b = float(user_2)
            c = float(user_3)
            d = float(user_4)
            try:
                y1 = (math.sqrt(a) + b ** 2) / (math.sqrt(b) - a ** 2) + math.sqrt((a * b) / (c * d))
                label1['text'] = '%.3f' % y1
            except ZeroDivisionError:
                label1['text'] = 'Помилка{0}'
        except ValueError:
            label1['text'] = 'Помилка!'
    root1 = Tk()
    root1.geometry('550x90')
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
    root1.wm_geometry("+%d+%d" % (x-100, y-300))
    root1.title('Перше завдання')
    root1['bg'] = 'seashell'

    entry1 = Entry(root1, width=15)
    entry2 = Entry(root1, width=15)
    entry3 = Entry(root1, width=15)
    entry4 = Entry(root1, width=15)
    button1 = Button(root1, text='Виконати', font="terminal 20", bg='LavenderBlush2', fg='maroon')
    label1 = Label(root1, font="terminal 15", bg='seashell', fg='brown')
    labelx1 = Label(root1, text='Введіть a:', font="terminal 20", bg='seashell', fg='brown')
    labelx2 = Label(root1, text='Введіть b:', font="terminal 20", bg='seashell', fg='brown')
    labelx3 = Label(root1, text='Введіть c:', font="terminal 20", bg='seashell', fg='brown')
    labelx4 = Label(root1, text='Введіть d:', font="terminal 20", bg='seashell', fg='brown')
    labelxr = Label(root1, text='Результат:', font="terminal 20", bg='seashell', fg='brown')
    test_label = Label(root1, text='             ', font="terminal 20", bg='seashell', fg='brown')

    entry1.grid(row=0, column=1)
    entry2.grid(row=0, column=4)
    entry3.grid(row=1, column=1)
    entry4.grid(row=1, column=4)
    button1.grid(row=2, column=4)
    label1.grid(row=2, column=1)
    labelx1.grid(row=0, column=0)
    labelx2.grid(row=0, column=3)
    labelx3.grid(row=1, column=0)
    labelx4.grid(row=1, column=3)
    labelxr.grid(row=2, column=0)
    test_label.grid(row=0, column=2)

    button1.bind("<Button-1>", result_1)

    root1.mainloop()


def window2(event):
    def result_2(event2):
        """Алгоритм 2"""
        user_1 = entry1.get()
        user_2 = entry2.get()
        user_3 = entry3.get()
        try:
            a = float(user_1)
            c = float(user_2)
            k = float(user_3)
            if k < 10:
                y2 = (a + c) ** 4 + (a - c) ** 2
                label1['text'] = y2
            else:
                y2 = (a - c) ** 3 + (a + c) ** 2
                label1['text'] = y2
        except ValueError:
            label1['text'] = 'Помилка!'

    root1 = Tk()
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
    root1.wm_geometry("+%d+%d" % (x-80, y-240))
    root1.title('Друге завдання')
    root1['bg'] = 'seashell'

    entry1 = Entry(root1, width=10)
    entry2 = Entry(root1, width=10)
    entry3 = Entry(root1, width=10)
    button1 = Button(root1, text='Виконати', font="terminal 15", bg='LavenderBlush2', fg='maroon')
    label1 = Label(root1, font="terminal 20", bg='seashell', fg='brown')
    labelx1 = Label(root1, text='Введіть a:', font="terminal 20", bg='seashell', fg='brown')
    labelx2 = Label(root1, text='Введіть c:', font="terminal 20", bg='seashell', fg='brown')
    labelx3 = Label(root1, text='Введіть k:', font="terminal 20", bg='seashell', fg='brown')
    labelxr = Label(root1, text='Результат:', font="terminal 20", bg='seashell', fg='brown')
    test_label = Label(root1, text='             ', font="terminal 20", bg='seashell', fg='brown')

    entry1.grid(row=0, column=1)
    entry2.grid(row=0, column=4)
    entry3.grid(row=1, column=1)
    button1.grid(row=2, column=4)
    label1.grid(row=2, column=1)
    labelx1.grid(row=0, column=0)
    labelx2.grid(row=0, column=3)
    labelx3.grid(row=1, column=0)
    labelxr.grid(row=2, column=0)
    test_label.grid(row=2, column=2)

    button1.bind("<Button-1>", result_2)

    root1.mainloop()


def window3(event):
    def result_3(event3):
        """Алгоритм 3"""
        user_1 = entry1.get()
        user_2 = entry2.get()
        user_3 = entry3.get()
        f = 0
        try:
            a = float(user_1)
            b = float(user_2)
            p = int(user_3)
            for i in range(1, p + 1):
                for j in range(1, p + 1):
                    for k in range(1, p + 1):
                        f += i ** 3 * j ** 2 * k * math.sqrt(a + b)
            label1['text'] = f
        except ValueError:
            label1['text'] = 'Помилка!'
    root1 = Tk()
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
    root1.wm_geometry("+%d+%d" % (x-80, y-160))
    root1.title('Третє завдання')
    root1['bg'] = 'seashell'

    entry1 = Entry(root1, width=10)
    entry2 = Entry(root1, width=10)
    entry3 = Entry(root1, width=10)
    button1 = Button(root1, text='Виконати', font="terminal 20", bg='LavenderBlush2', fg='maroon')
    label1 = Label(root1, font="terminal 20", bg='seashell', fg='brown')
    labelx1 = Label(root1, text='Введіть a:', font="terminal 20", bg='seashell', fg='brown')
    labelx2 = Label(root1, text='Введіть b:', font="terminal 20", bg='seashell', fg='brown')
    labelx3 = Label(root1, text='Введіть p:', font="terminal 20", bg='seashell', fg='brown')
    labelxr = Label(root1, text='Результат:', font="terminal 20", bg='seashell', fg='brown')
    test_label = Label(root1, text='             ', font="terminal 20", bg='seashell', fg='brown')

    entry1.grid(row=0, column=1)
    entry2.grid(row=0, column=4)
    entry3.grid(row=1, column=1)
    button1.grid(row=2, column=4)
    label1.grid(row=2, column=1)
    labelx1.grid(row=0, column=0)
    labelx2.grid(row=0, column=3)
    labelx3.grid(row=1, column=0)
    labelxr.grid(row=2, column=0)
    test_label.grid(row=2, column=2)

    button1.bind("<Button-1>", result_3)

    root1.mainloop()


root = Tk()
root.title('Головне Меню')
root['bg'] = 'seashell'
root.geometry('280x110')
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.wm_geometry("+%d+%d" % (x, y))

label1 = Label(root, text='Перше завдання   ', font="terminal 20", bg='seashell', fg='brown')
button1 = Button(root, text='Перейти', font="terminal 20", bg='LavenderBlush2', fg='maroon')
label2 = Label(root, text='Друге завдання   ', font="terminal 20", bg='seashell', fg='brown')
button2 = Button(root, text='Перейти', font="terminal 20", bg='LavenderBlush2', fg='maroon', )
label3 = Label(root, text='Третє завдання   ', font="terminal 20", bg='seashell', fg='brown')
button3 = Button(root, text='Перейти', font="terminal 20", bg='LavenderBlush2', fg='maroon')

label1.grid(row=0, column=0)
button1.grid(row=0, column=1)
label2.grid(row=1, column=0)
button2.grid(row=1, column=1)
label3.grid(row=2, column=0)
button3.grid(row=2, column=1)

button1.bind("<Button-1>", window1)
button2.bind("<Button-1>", window2)
button3.bind("<Button-1>", window3)

root.mainloop()

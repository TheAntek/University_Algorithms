from tkinter import *


def window1(event):
    def result_1(event1):
        """Алгоритм 1"""
        user_1 = entry1.get()
        user_2 = entry2.get()
        try:
            user_1 = float(user_1)
            user_2 = float(user_2)
            y1 = abs(user_1 - user_2) + abs(user_1 + user_2) / 6
            label1['text'] = y1
        except ValueError:
            label1['text'] = 'Помилка!'
    root1 = Tk()
    root1.title('Перше завдання')

    entry1 = Entry(root1, width=10)
    entry2 = Entry(root1, width=10)
    button1 = Button(root1, text='Виконати', font=10, bg='black', fg='orange')
    label1 = Label(root1)
    labelx1 = Label(root1, text='Введіть a:')
    labelx2 = Label(root1, text='Введіть z:')
    labelx3 = Label(root1, text='Результат:')
    test_label = Label(root1, text='             ')

    entry1.grid(row=0, column=1)
    entry2.grid(row=0, column=4)
    button1.grid(row=1, column=2)
    label1.grid(row=2, column=1)
    labelx1.grid(row=0, column=0)
    labelx2.grid(row=0, column=3)
    labelx3.grid(row=2, column=0)
    test_label.grid(row=2, column=2)

    button1.bind("<Button-1>", result_1)

    root1.mainloop()


def window2(event):
    def result_2(event2):
        """Алгоритм 2"""
        user_1 = entry1.get()
        user_2 = entry2.get()
        try:
            user_1 = float(user_1)
            user_2 = float(user_2)
            if user_1 > 10:
                y2 = 2 * user_1 ** 2 + user_2
                label1['text'] = y2
            else:
                y2 = 2 * user_1 ** 2 - user_2
                label1['text'] = y2
        except ValueError:
            label1['text'] = 'Помилка!'

    root1 = Tk()
    root1.title('Друге завдання')

    entry1 = Entry(root1, width=10)
    entry2 = Entry(root1, width=10)
    button1 = Button(root1, text='Виконати', font=10, bg='black', fg='orange')
    label1 = Label(root1)
    labelx1 = Label(root1, text='Введіть a:')
    labelx2 = Label(root1, text='Введіть x:')
    labelx3 = Label(root1, text='Результат:')
    test_label = Label(root1, text='             ')

    entry1.grid(row=0, column=1)
    entry2.grid(row=0, column=4)
    button1.grid(row=1, column=2)
    label1.grid(row=2, column=1)
    labelx1.grid(row=0, column=0)
    labelx2.grid(row=0, column=3)
    labelx3.grid(row=2, column=0)
    test_label.grid(row=2, column=2)

    button1.bind("<Button-1>", result_2)

    root1.mainloop()


def window3(event):
    def result_1(event3):
        """Алгоритм 3"""
        user_1 = entry1.get()
        user_2 = entry2.get()
        f = 1
        try:
            user_1 = float(user_1)
            user_2 = float(user_2)
            for i in range(5):
                try:
                    f *= (user_1 ** 3 - user_2 ** 2) / (user_1 * user_2)
                except ZeroDivisionError:
                    f = 'Помилка! {0}'
                    break
            label1['text'] = f
        except ValueError:
            label1['text'] = 'Помилка!'
    root1 = Tk()
    root1.title('Третє завдання')

    entry1 = Entry(root1, width=10)
    entry2 = Entry(root1, width=10)
    button1 = Button(root1, text='Виконати', font=10, bg='black', fg='orange')
    label1 = Label(root1)
    labelx1 = Label(root1, text='Введіть a:')
    labelx2 = Label(root1, text='Введіть z:')
    labelx3 = Label(root1, text='Результат:')
    test_label = Label(root1, text='             ')

    entry1.grid(row=0, column=1)
    entry2.grid(row=0, column=4)
    button1.grid(row=1, column=2)
    label1.grid(row=2, column=1)
    labelx1.grid(row=0, column=0)
    labelx2.grid(row=0, column=3)
    labelx3.grid(row=2, column=0)
    test_label.grid(row=2, column=2)

    button1.bind("<Button-1>", result_1)

    root1.mainloop()


root = Tk()
root.title('Головне Меню')
root.geometry('350x120')
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.wm_geometry("+%d+%d" % (x, y))

label1 = Label(root, text='          Перше завдання     ', font=10)
button1 = Button(root, text='Перейти', font=12, bg='black', fg='yellow')
label2 = Label(root, text='          Друге завдання     ', font=10)
button2 = Button(root, text='Перейти', font=12, bg='black', fg='yellow')
label3 = Label(root, text='          Третє завдання     ', font=10)
button3 = Button(root, text='Перейти', font=12, bg='black', fg='yellow')

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

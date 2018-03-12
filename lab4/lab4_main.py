from tkinter import *
from AMO.lab4.lab4_func import half_interval_method, func


def gui():
    def my_func(event):
        a = entry1.get()
        b = entry2.get()
        e = entry3.get()
        try:
            a = int(a)
            b = int(b)
            e = float(e)
            result = half_interval_method(func, a, b, e)
            label_res['text'] = result
        except ValueError:
            label_res['text'] = 'Error'

    root = Tk()
    root["bg"] = "honeydew"
    root.title('Лабораторна робота №4 (Метод половинного ділення)')
    root.geometry('830x320')
    x1 = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
    y1 = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
    root.wm_geometry("+%d+%d" % (x1-310, y1-140))

    entry1 = Entry(root, width=15, bg='lavender', fg='purple4', relief=GROOVE, bd=2, font="terminal 15")
    entry2 = Entry(root, width=15, bg='lavender', fg='purple4', relief=GROOVE, bd=2, font="terminal 15")
    entry3 = Entry(root, width=15, bg='lavender', fg='purple4', relief=GROOVE, bd=2, font="terminal 15")

    label_name = Label(root, text='Функція:', width=15, height=5, bg='honeydew', fg='dark green', font="terminal 15")
    label_func = Label(root, text='x^3 + 2x - 4 = 0', width=25, height=5, bg='honeydew', fg='deep pink',
                       font="terminal 15")
    label_1 = Label(root, text='Введіть a:', width=15, height=5, bg='honeydew', fg='dark green',
                    font="terminal 15")
    label_2 = Label(root, text='Введіть b:', width=15, height=5, bg='honeydew', fg='dark green',
                    font="terminal 15")
    label_3 = Label(root, text='Введіть точність:', width=20, height=5, bg='honeydew', fg='dark green',
                    font="terminal 15")
    label_4 = Label(root, text='Результат:', width=15, height=5, bg='honeydew', fg='dark green',
                    font="terminal 15")
    label_res = Label(root, width=20, height=5, bg='honeydew', fg='deep pink', font="terminal 15")

    button1 = Button(root, text='Виконати', width=15, height=2, bg='lavender', fg='purple4', font="terminal 15",
                     relief=GROOVE, overrelief=RIDGE, bd=4)

    entry1.grid(row=1, column=1)
    entry2.grid(row=2, column=1)
    entry3.grid(row=0, column=3)

    label_name.grid(row=0, column=0)
    label_func.grid(row=0, column=1)
    label_1.grid(row=1, column=0)
    label_2.grid(row=2, column=0)
    label_3.grid(row=0, column=2)
    label_4.grid(row=2, column=2)
    label_res.grid(row=2, column=3)

    button1.grid(row=1, column=3)

    button1.bind("<Button-1>", my_func)

    root.mainloop()


if __name__ == '__main__':
    gui()

from tkinter import *
import random
import time


def selection_sort(ar):
    for i in range(len(ar)):
        x = i
        for z in range(x + 1, len(ar)):
            if ar[x] > ar[z]:
                x = z
        ar[i], ar[x] = ar[x], ar[i]
    return ar


def func(event):
    user_1 = entry1.get()
    try:
        size = int(user_1)
        apple = [random.randint(0, 1000) for i in range(size)]
        time_start = time.clock()
        selection_sort(apple)
        time_end = time.clock()
        label_res['text'] = time_end-time_start, '(сек)'
    except ValueError:
        label_res['text'] = 'Помилка!'


def func_file(event_file):
    f = open('lab2.txt')
    user_1 = f.read()
    try:
        size = int(user_1)
        apple = [random.randint(0, 1000) for i in range(size)]
        time_start = time.clock()
        selection_sort(apple)
        time_end = time.clock()
        label_res['text'] = time_end-time_start, '(сек)'
    except ValueError:
        label_res['text'] = 'Помилка!'


root = Tk()
root["bg"] = "honeydew"
root.title('Лабораторна 2')
root.geometry('567x350')
x1 = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y1 = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.wm_geometry("+%d+%d" % (x1-170, y1-100))

entry1 = Entry(root, width=30, bg='lavender', fg='purple4', relief=GROOVE, bd=2)
button1 = Button(root, text='Виконати', width=27, height=5, bg='lavender', fg='purple4', font="terminal 15",
                 relief=GROOVE, overrelief=RIDGE, bd=4)
button2 = Button(root, text='Виконати (файл)', width=27, height=5, bg='lavender', fg='purple4', font="terminal 15",
                 relief=GROOVE, overrelief=RIDGE, bd=4)
label_res = Label(root, width=25, height=5, bg='honeydew', fg='purple4', font="terminal 15")
label_n = Label(root, text='Введіть розмір масиву:', width=25, height=5, bg='honeydew', fg='dark green',
                font="terminal 15")
label_r = Label(root, text='Час сортування:', width=25, height=5, bg='honeydew', fg='dark green', font="terminal 15")

entry1.grid(row=0, column=1)
button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
label_res.grid(row=2, column=1)
label_n.grid(row=0, column=0)
label_r.grid(row=2, column=0)

button1.bind("<Button-1>", func)
button2.bind("<Button-1>", func_file)

root.mainloop()

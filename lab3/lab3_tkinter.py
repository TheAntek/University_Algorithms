import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pylab
from tkinter import *


def f(x):
    return x*np.cos(x+np.log(1+x))


def lagrange_pol(nodes, values):
    n = nodes.size

    def p(x):
        polynomial = 0
        for j in range(n):
            def product(j, n):
                total = 1
                for i in range(n):
                    if i == j:
                        continue
                    xi = nodes[i]
                    xj = nodes[j]
                    total *= (x - xi) / (xj - xi)
                return total

            polynomial += product(j, n) * values[j]
        return polynomial
    return p


def func(event):
    user_1 = entry1.get()
    user_2 = entry2.get()
    user_3 = entry3.get()
    user_4 = entry4.get()
    try:
        a = float(user_1)
        b = float(user_2)
        n = int(user_3)
        x = int(user_4)
        n2 = n+1

        step = (b - a) / n
        step2 = (b - a) / n2

        x_nodes = np.arange(a, b + 0.1, step)
        f_values = f(x_nodes)

        x_nodes2 = np.arange(a, b + 0.1, step2)
        f_values2 = f(x_nodes2)

        pol = lagrange_pol(x_nodes, f_values)
        pol2 = lagrange_pol(x_nodes2, f_values2)

        x_arg = np.arange(0, 5, 0.01)

        fig = plt.figure()
        plt.subplot(211)
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title('Інтерполяція Лагранжа\n(інтервал [{}; {}], Точки: {})'.format(a, b, n))

        plt.plot(x_arg, f(x_arg), label='оригінал')
        plt.plot(x_arg, pol(x_arg), label='лагранж')
        plt.axis([a, b, -3, 5])
        plt.legend(loc=3, prop={'size': 8})

        plt.subplot(212)
        plt.xlabel('x')
        plt.ylabel('R(x)')
        plt.title('Відхилення (Похибка)')

        plt.plot(x_arg, f(x_arg) - pol(x_arg))
        plt.axis([a, b, -0.00002, 0.00002])

        fig.subplots_adjust(hspace=0.4)
        fig = pylab.gcf()
        fig.canvas.set_window_title('Lagrange interpolation')

        plt.show()

        poh_int = pol(x) - pol2(x)
        label_res1['text'] = f(x)
        label_res2['text'] = abs(pol(x) - f(x))
        label_res3['text'] = abs(1 - (pol(x) - f(x)) / poh_int)

    except ValueError:
        print('Error')


root = Tk()
root["bg"] = "honeydew"
root.title('Лабораторна 3')
root.geometry('1100x435')
x1 = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y1 = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.wm_geometry("+%d+%d" % (x1-545, y1-190))

entry1 = Entry(root, width=15, bg='lavender', fg='purple4', relief=GROOVE, bd=2, font="terminal 15")
entry2 = Entry(root, width=15, bg='lavender', fg='purple4', relief=GROOVE, bd=2, font="terminal 15")
entry3 = Entry(root, width=15, bg='lavender', fg='purple4', relief=GROOVE, bd=2, font="terminal 15")
entry4 = Entry(root, width=5, bg='lavender', fg='purple4', relief=GROOVE, bd=2, font="terminal 15")
button1 = Button(root, text='Виконати', width=55, height=5, bg='lavender', fg='purple4', font="terminal 15",
                 relief=GROOVE, overrelief=RIDGE, bd=4)
label_1 = Label(root, text='Введіть початок:', width=25, height=5, bg='honeydew', fg='dark green',
                font="terminal 15")
label_2 = Label(root, text='Введіть кінець:', width=25, height=5, bg='honeydew', fg='dark green',
                font="terminal 15")
label_3 = Label(root, text='Введіть к-сть вузлів:', width=25, height=5, bg='honeydew', fg='dark green',
                font="terminal 15")
label_4 = Label(root, text='Введіть X:', width=25, height=5, bg='honeydew', fg='dark green',
                font="terminal 15")
label_5 = Label(root, text='Результат Y:', width=25, height=5, bg='honeydew', fg='dark green',
                font="terminal 15")
label_6 = Label(root, text='Похибка:', width=25, height=5, bg='honeydew', fg='dark green',
                font="terminal 15")
label_7 = Label(root, text='Розмитість похибки:', width=25, height=5, bg='honeydew', fg='dark green',
                font="terminal 15")
label_res1 = Label(root, width=25, height=5, bg='honeydew', fg='purple4', font="terminal 15")
label_res2 = Label(root, width=25, height=5, bg='honeydew', fg='purple4', font="terminal 15")
label_res3 = Label(root, width=25, height=5, bg='honeydew', fg='purple4', font="terminal 15")

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
entry3.grid(row=2, column=1)
entry4.grid(row=0, column=3)
label_1.grid(row=0, column=0)
label_2.grid(row=1, column=0)
label_3.grid(row=2, column=0)
label_4.grid(row=0, column=2)
label_5.grid(row=1, column=2)
label_6.grid(row=2, column=2)
label_7.grid(row=3, column=2)
label_res1.grid(row=1, column=3)
label_res2.grid(row=2, column=3)
label_res3.grid(row=3, column=3)
button1.grid(row=3, column=0, columnspan=2)

button1.bind("<Button-1>", func)

root.mainloop()

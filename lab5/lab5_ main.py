from tkinter import *
from AMO.lab5.lab5_func import gauss


def gui():
    def my_func(event):

        try:
            a = (int(entry1.get()), int(entry2.get()), int(entry3.get()), int(entry4.get()))
            b = (int(entry5.get()), int(entry6.get()), int(entry7.get()), int(entry8.get()))
            c = (int(entry9.get()), int(entry10.get()), int(entry11.get()), int(entry12.get()))
            matrix = [a, b, c]
            try:
                result = gauss(matrix)
                res_labels = [label_res1, label_res2, label_res3]
                for i in range(len(result)):
                    res_labels[i]['text'] = round(result[i], 2)
            except IndexError:
                print('index error')

        except ValueError:
            print('value error')

    root = Tk()
    root["bg"] = "honeydew"
    root.title('Лабораторна робота №5')
    root.geometry('540x325')
    x1 = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
    y1 = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
    root.wm_geometry("+%d+%d" % (x1 - 190, y1 - 130))

    entry1 = Entry(root, width=2, bg='lavender', fg='purple4', relief=GROOVE, bd=2, font="terminal 15")
    entry2 = Entry(root, width=2, bg='lavender', fg='purple4', relief=GROOVE, bd=2, font="terminal 15")
    entry3 = Entry(root, width=2, bg='lavender', fg='purple4', relief=GROOVE, bd=2, font="terminal 15")
    entry4 = Entry(root, width=2, bg='lavender', fg='purple4', relief=GROOVE, bd=2, font="terminal 15")
    entry5 = Entry(root, width=2, bg='lavender', fg='purple4', relief=GROOVE, bd=2, font="terminal 15")
    entry6 = Entry(root, width=2, bg='lavender', fg='purple4', relief=GROOVE, bd=2, font="terminal 15")
    entry7 = Entry(root, width=2, bg='lavender', fg='purple4', relief=GROOVE, bd=2, font="terminal 15")
    entry8 = Entry(root, width=2, bg='lavender', fg='purple4', relief=GROOVE, bd=2, font="terminal 15")
    entry9 = Entry(root, width=2, bg='lavender', fg='purple4', relief=GROOVE, bd=2, font="terminal 15")
    entry10 = Entry(root, width=2, bg='lavender', fg='purple4', relief=GROOVE, bd=2, font="terminal 15")
    entry11 = Entry(root, width=2, bg='lavender', fg='purple4', relief=GROOVE, bd=2, font="terminal 15")
    entry12 = Entry(root, width=2, bg='lavender', fg='purple4', relief=GROOVE, bd=2, font="terminal 15")

    label_0 = Label(root, text='   ', height=1, bg='honeydew', fg='dark green', font="terminal 15")
    label_01 = Label(root, text='        ', height=1, bg='honeydew', fg='dark green', font="terminal 15")
    label_x1 = Label(root, text='x1+', width=3, height=2, bg='honeydew', fg='dark green', font="terminal 15")
    label_x2 = Label(root, text='x1+', width=3, height=2, bg='honeydew', fg='dark green', font="terminal 15")
    label_x3 = Label(root, text='x1+', width=3, height=2, bg='honeydew', fg='dark green', font="terminal 15")
    label_x4 = Label(root, text='x2+', width=3, height=2, bg='honeydew', fg='dark green', font="terminal 15")
    label_x5 = Label(root, text='x2+', width=3, height=2, bg='honeydew', fg='dark green', font="terminal 15")
    label_x6 = Label(root, text='x2+', width=3, height=2, bg='honeydew', fg='dark green', font="terminal 15")
    label_x7 = Label(root, text='x3=', width=3, height=2, bg='honeydew', fg='dark green', font="terminal 15")
    label_x8 = Label(root, text='x3=', width=3, height=2, bg='honeydew', fg='dark green', font="terminal 15")
    label_x9 = Label(root, text='x3=', width=3, height=2, bg='honeydew', fg='dark green', font="terminal 15")

    label_text = Label(root, text='Результати:', height=1, bg='honeydew', fg='purple4', font="terminal 15")
    label_r1 = Label(root, text='x1=', width=3, height=1, bg='honeydew', fg='dark green', font="terminal 15")
    label_r2 = Label(root, text='x2=', width=3, height=1, bg='honeydew', fg='dark green', font="terminal 15")
    label_r3 = Label(root, text='x3=', width=3, height=1, bg='honeydew', fg='dark green', font="terminal 15")

    label_res1 = Label(root, width=3, height=1, bg='honeydew', fg='deep pink', font="terminal 15")
    label_res2 = Label(root, width=3, height=1, bg='honeydew', fg='deep pink', font="terminal 15")
    label_res3 = Label(root, width=3, height=1, bg='honeydew', fg='deep pink', font="terminal 15")

    button1 = Button(root, text='Виконати', width=15, height=2, bg='lavender', fg='purple4', font="terminal 15",
                     relief=GROOVE, overrelief=RIDGE, bd=4)

    entry1.grid(row=1, column=1)
    entry2.grid(row=1, column=3)
    entry3.grid(row=1, column=5)
    entry4.grid(row=1, column=7)
    entry5.grid(row=2, column=1)
    entry6.grid(row=2, column=3)
    entry7.grid(row=2, column=5)
    entry8.grid(row=2, column=7)
    entry9.grid(row=3, column=1)
    entry10.grid(row=3, column=3)
    entry11.grid(row=3, column=5)
    entry12.grid(row=3, column=7)

    label_0.grid(row=0, column=0)
    label_01.grid(row=4, column=8)
    label_x1.grid(row=1, column=2)
    label_x2.grid(row=2, column=2)
    label_x3.grid(row=3, column=2)
    label_x4.grid(row=1, column=4)
    label_x5.grid(row=2, column=4)
    label_x6.grid(row=3, column=4)
    label_x7.grid(row=1, column=6)
    label_x8.grid(row=2, column=6)
    label_x9.grid(row=3, column=6)

    label_text.grid(row=5, column=1, columnspan=3)
    label_r1.grid(row=6, column=1)
    label_r2.grid(row=7, column=1)
    label_r3.grid(row=8, column=1)
    label_res1.grid(row=6, column=2)
    label_res2.grid(row=7, column=2)
    label_res3.grid(row=8, column=2)

    button1.grid(row=2, column=9)

    button1.bind("<Button-1>", my_func)

    root.mainloop()


if __name__ == '__main__':
    gui()

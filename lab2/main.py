import time
import tkinter as tk
import random
import traceback
from tkinter import messagebox

root = tk.Tk()
root.grid_columnconfigure(0, weight=1)
lbl_exceptions = tk.Label(root, background="white", width=90, height=20, anchor="w", justify="left")
lbl_exceptions.grid(row=0, column=0, columnspan=5, sticky='ew')


def show_error(self, *args):
    from datetime import datetime
    err = traceback.format_exception(*args)
    now = datetime.now()
    dt_string = now.strftime("%d.%m.%Y - %H:%M:%S")
    text = dt_string + "\n"
    for e in err:
        text += e + "\n"
    lbl_exceptions.config(text=text)

    fp = open('exceptions.txt', 'a')
    fp.write(text)
    fp.close()
    # messagebox.showerror('Exception', err)


tk.Tk.report_callback_exception = show_error


def lab2_btn():
    window = tk.Toplevel(root)
    window.title("Виндоус Форма")
    window.geometry("780x330+5+400")

    # def callback(sv):
    #     print(sv.get())

    def sel():
        # selection = "You selected the option " + str(var.get())
        # lbl_select.config(text=selection)
        match int(var.get()):
            case 1:
                for entry in ins:
                    entry.config(state='normal')
                ent_frequency.config(state='disabled')
            case 2:
                for entry in ins:
                    entry.config(state='disabled')
                ent_frequency.config(state='disabled')
            case 3:
                for entry in ins:
                    entry.config(state='disabled')
                ent_frequency.config(state='normal')

    lbl_count = tk.Label(window, text="Выберите способ формирования массива:")
    lbl_count.grid(row=0, column=0, columnspan=10, sticky="w")

    var = tk.IntVar()
    R1 = tk.Radiobutton(window, text="Вручную", variable=var, value=1, command=sel)
    R1.select()
    R1.grid(row=1, column=0, columnspan=10, sticky="w")

    R2 = tk.Radiobutton(window, text="Случайно", variable=var, value=2, command=sel)
    R2.grid(row=2, column=0, columnspan=10, sticky="w")

    R3 = tk.Radiobutton(window, text="Случайно с заданной частотой", variable=var, value=3, command=sel)
    R3.grid(row=3, column=0, columnspan=10, sticky="w")

    # lbl_select = tk.Label(window)
    # lbl_select.grid(row=4, column=0, columnspan=10)

    # k = tk.StringVar()
    # k.trace("w", lambda name, index, mode, sv=k: callback(sv))
    lbl_k = tk.Label(window, text="Введиите число k:")
    ent_k = tk.Entry(window, width=13)
    lbl_k.grid(row=1, column=11, columnspan=5, sticky="w")
    ent_k.grid(row=2, column=11, columnspan=5, sticky="w")

    # frequency = tk.StringVar()
    # frequency.trace("w", lambda name, index, mode, sv=frequency: callback(sv))
    lbl_frequency = tk.Label(window, text="Частота:")
    ent_frequency = tk.Entry(window, width=13, state="disabled")
    lbl_frequency.grid(row=1, column=16, columnspan=5, sticky="w")
    ent_frequency.grid(row=2, column=16, columnspan=5, sticky="w")

    def alg():
        mine = tk.Entry(textvariable=tk.IntVar(value=100))
        if int(var.get()) == 2:
            for entry in ins:
                tmp = random.randint(1, 99)
                entry.config(textvariable=tk.IntVar(value=tmp))
                if tmp < int(mine.get()):
                    mine = entry
        if int(var.get()) == 3:
            for entry in ins:
                tmp = random.randint(1, int(ent_frequency.get()))
                entry.config(textvariable=tk.IntVar(value=tmp))
                if tmp < int(mine.get()):
                    mine = entry

        start = time.time() * 1000000
        if int(check_var1.get()) == 0:
            count = 0
            for entry in outs:
                if count < 10:
                    entry.config(text=int(search(count)) + count)
                else:
                    entry.config(text=int(search(count)) - count)
                count += 1

            def zer():
                mine.config(textvariable=tk.IntVar(value=0))

            window.after(5000, zer)
            time.sleep(5)

            def repl():
                count = 0
                tmp = int()
                for entry in outs:
                    if int(ent_k.get()) == count:
                        tmp = entry.cget("text")
                        entry.config(textvariable=tk.IntVar(value=int(search(int(ent_k.get())))))
                        break
                    else:
                        count += 1
                count = 0
                for entry in ins:
                    if int(ent_k.get()) == count:
                        entry.config(textvariable=tk.IntVar(value=tmp))
                        break
                    else:
                        count += 1

            window.after(7500, repl)
            time.sleep(2.5)
        elif int(check_var1.get()) == 1:
            from threading import Thread
            def for_first():
                count = 0
                for entry in outs:
                    if count < 10:
                        entry.config(text=int(search(count)) + count)
                        count += 1
                    else:
                        break

                def zer():
                    mine.config(textvariable=tk.IntVar(value=0))

                window.after(5000, zer)
                time.sleep(5)

            def for_second():
                count = len(outs) - 1
                for entry in reversed(outs):
                    if count >= 10:
                        entry.config(text=int(search(count)) - count)
                        count -= 1
                    else:
                        break

                def repl():
                    count = 0
                    tmp = int()
                    for entry in outs:
                        if int(ent_k.get()) == count:
                            tmp = entry.cget("text")
                            entry.config(textvariable=tk.IntVar(value=int(search(int(ent_k.get())))))
                            break
                        else:
                            count += 1
                    count = 0
                    for entry in ins:
                        if int(ent_k.get()) == count:
                            entry.config(textvariable=tk.IntVar(value=tmp))
                            break
                        else:
                            count += 1

                window.after(7500, repl)
                time.sleep(2.5)

            th1 = Thread(target=for_first, args=())
            th2 = Thread(target=for_second, args=())
            th1.start()
            th2.start()
            # th1.join()
            # th1.join()
        end = time.time() * 1000000 - start
        if end > 1000:
            if end > 10000:
                if end > 10000000:
                    txttime = "runtime: {:0.2f} seconds".format(end / 10000000)
                else:
                    txttime = "runtime: {:0.2f} milliseconds".format(end / 10000)
            else:
                txttime = "runtime: {:0.2f} microseconds".format(end / 1000)
        else:
            txttime = "runtime: {:0.2f} nanoseconds".format(end)
        # print(end)
        lbl_time.config(text=txttime)

    def search(i):
        count = 0
        for entry in ins:
            if i == count:
                return entry.get()
            else:
                count += 1

    def dop():
        # import matplotlib as plt
        # height = []
        # for entry in ins:
        #     height.append(int(entry.get()))
        #
        window2 = tk.Toplevel(window)
        window2.title("Задача про гистограмму с водой")
        window2.geometry("500x330+825+400")
        # plt.hist(height, 20)
        # plt.show()
        # import tkinter as tk
        import matplotlib

        matplotlib.use('TkAgg')

        from matplotlib.figure import Figure
        from matplotlib.backends.backend_tkagg import (
            FigureCanvasTkAgg,
            NavigationToolbar2Tk
        )

        class App(tk.Tk):
            def __init__(self):
                # super().__init__()
                # self.title('Задача про гистограмму с водой')

                histo = []
                for entry in ins:
                    histo.append(int(entry.get()))

                left_maxes = histo.copy()
                left_max = histo[0]
                for i in range(len(histo)):
                    left_max = max(left_max, histo[i])
                    left_maxes[i] = left_max

                sum = 0
                water = [0] * len(histo)

                # create a figure
                figure = Figure(figsize=(6, 4), dpi=100)

                # create FigureCanvasTkAgg object
                figure_canvas = FigureCanvasTkAgg(figure, master=window2)
                figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

                # create the toolbar
                # NavigationToolbar2Tk(figure_canvas, self)

                # create axes
                axes = figure.add_subplot()
                axes.bar([x for x in range(0, 20)], histo, label='Столбцы', color="black")
                axes.bar([x for x in range(0, 20)], water, bottom=histo, label='Вода', color="lightblue")

                right_max = histo[len(histo) - 1]
                for i in range(len(histo) - 1, 0, -1):
                    right_max = max(right_max, histo[i])
                    second_tallest = min(right_max, left_maxes[i])
                    if second_tallest > histo[i]:
                        water[i] = second_tallest - histo[i]
                        sum += water[i]
                print(sum)

                def draw_water():
                    figure.clear()
                    axes = figure.add_subplot()
                    axes.bar([x for x in range(0, 20)], histo, label='Столбцы', color="black")
                    axes.bar([x for x in range(0, 20)], water, bottom=histo, label='Вода', color="lightblue")
                    figure_canvas.draw_idle()

                window2.after(3000, draw_water)

        if __name__ == '__main__':
            app = App()
            app.mainloop()

    ins = []
    btn_length = tk.Button(window, text="Старт", command=alg, width=10)
    btn_length.grid(row=5, column=11, columnspan=5, sticky="w")

    btn_length = tk.Button(window, text="Доп", command=dop, width=10)
    btn_length.grid(row=5, column=16, columnspan=5, sticky="w")

    lbl_initm = tk.Label(window, text="Исходный массив:")
    lbl_initm.grid(row=5, column=0, columnspan=5, sticky="w")

    check_var1 = tk.IntVar()
    C1 = tk.Checkbutton(window, text="Многопоточность", variable=check_var1, onvalue=1, offvalue=0, height=5, width=15)
    C1.grid(row=5, column=6, columnspan=5, sticky="w")

    for x in range(20):
        text = tk.Label(window, width=3, text=x, background="white")
        text.grid(row=6, column=x)
        inp = tk.Entry(window, width=3)
        inp.grid(row=7, column=x)
        ins.append(inp)

    lbl_resm = tk.Label(window, text="Результирующий массив:")
    lbl_resm.grid(row=9, column=0, columnspan=5, sticky="w")

    # tk.Label(window, width=8).grid(row=6, column=0, columnspan=2, sticky="w")

    outs = []
    for x in range(20):
        text = tk.Label(window, width=3, text=x, background="white")
        text.grid(row=11, column=x)
        outp = tk.Label(window, width=3, background="white")
        outp.grid(row=12, column=x, pady=(3, 0))
        outs.append(outp)

    lbl_time = tk.Label(window, text="Время выполнения")
    lbl_time.grid(row=13, column=0, columnspan=5, sticky="w")

    window.mainloop()


def donothing():
    filewin = tk.Toplevel(root)
    lbl_nothing = tk.Label(filewin, text="There is nothing to see here", padx=100, pady=100)
    lbl_nothing.pack()


def about_btn():
    from PIL import ImageTk, Image

    filewin = tk.Toplevel(root)
    img = ImageTk.PhotoImage(Image.open("me.png"))
    about_photo_lbl = tk.Label(filewin, image=img)
    about_photo_lbl.grid(row=0)

    about_name_lbl = tk.Label(filewin, text="Vadim Dmitriev", font='Helvetica 18 bold')
    about_name_lbl.grid(row=1)

    about_description_lbl = tk.Label(filewin, text="I spent an hour on this screen")
    about_description_lbl.grid(row=2)

    about_description_lbl = tk.Label(filewin, text="(c) 2022-2022 State University of Aerospace Instrumentation.")
    about_description_lbl.grid(row=3)

    filewin.mainloop()


menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="ЛР 1", command=donothing)
filemenu.add_command(label="ЛР 2", command=lab2_btn)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.destroy)
menubar.add_cascade(label="Технологии и методы программирования", menu=filemenu)

helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="About...", command=about_btn)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

root.mainloop()

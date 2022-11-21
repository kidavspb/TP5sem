import time
import tkinter as tk
import random
import traceback
from tkinter import messagebox, filedialog
from PIL import ImageGrab, ImageTk, Image
import numpy as np

root = tk.Tk()
root.geometry("850x200")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

lbl_exceptions = tk.Label(root, background="white", anchor="nw", justify="left")
lbl_exceptions.grid(row=0, column=0, columnspan=5, padx=5, pady=5, sticky=tk.E + tk.W + tk.S + tk.N)


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

    def alg2():
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

    def dop2():
        window2 = tk.Toplevel(window)
        window2.title("Задача про гистограмму с водой")
        window2.geometry("500x330+825+400")
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
    btn_length = tk.Button(window, text="Старт", command=alg2, width=10)
    btn_length.grid(row=5, column=11, columnspan=5, sticky="w")

    btn_length = tk.Button(window, text="Доп", command=dop2, width=10)
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


# ——————————————————————————————————————

def lab3_btn():
    window = tk.Toplevel(root)
    window.geometry("850x500+5+300")

    def fourie():
        window3 = tk.Toplevel(window)
        window3.title("Сигналы Фурье")
        window3.geometry("550x667+880+30")

        def callback(sv):
            # print(sv.get())
            sel()

        svA = tk.IntVar()
        svT = tk.IntVar()
        svN = tk.IntVar()
        svA.trace("w", lambda name, index, mode, sv=svA: callback(sv))
        svT.trace("w", lambda name, index, mode, sv=svT: callback(sv))
        svN.trace("w", lambda name, index, mode, sv=svN: callback(sv))

        amplitude_lbl = tk.Label(window3, text="Амплитуда (A):")
        amplitude_lbl.place(x=0, y=0)
        amplitude_scl = tk.Scale(window3, variable=svA, from_=1, to=100, orient=tk.HORIZONTAL)
        amplitude_scl.place(x=110, y=0)

        period_lbl = tk.Label(window3, text="Период (T):")
        period_lbl.place(x=0, y=50)
        period_scl = tk.Scale(window3, variable=svT, from_=1, to=100, orient=tk.HORIZONTAL)
        period_scl.place(x=110, y=50)

        count_lbl = tk.Label(window3, text="Количество (N):")
        count_lbl.place(x=0, y=100)
        count_lbl = tk.Scale(window3, variable=svN, from_=1, to=100, orient=tk.HORIZONTAL)
        count_lbl.place(x=110, y=100)

        # amplitude_lbl = tk.Label(window3, text="Амплитуда (A):")
        # amplitude_lbl.place(x=0, y=0)
        # amplitude_ent = tk.Entry(window3, width=10, textvariable=svA)
        # amplitude_ent.place(x=110, y=0)

        # period_lbl = tk.Label(window3, text="Период (T):")
        # period_lbl.place(x=0, y=20)
        # period_ent = tk.Entry(window3, width=10, textvariable=svT)
        # period_ent.place(x=110, y=20)

        # count_lbl = tk.Label(window3, text="Количество (N):")
        # count_lbl.place(x=0, y=40)
        # count_ent = tk.Entry(window3, width=10, textvariable=svN)
        # count_ent.place(x=110, y=40)

        def plot(S):
            # import tkinter as tk
            from matplotlib.figure import Figure
            from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

            # the figure that will contain the plot
            fig = Figure(figsize=(5, 5), dpi=100)

            # adding the subplot
            plot1 = fig.add_subplot(111)

            # plotting the graph
            plot1.plot(S)

            # creating the Tkinter canvas
            # containing the Matplotlib figure
            canvas = FigureCanvasTkAgg(fig, master=window3)
            canvas.draw()

            # placing the canvas on the Tkinter window
            canvas.get_tk_widget().pack()

            # creating the Matplotlib toolbar
            # toolbar = NavigationToolbar2Tk(canvas, window3)
            # toolbar.update()

            # placing the toolbar on the Tkinter window
            canvas.get_tk_widget().place(x=0, y=170)

        def sel():
            selection = ""
            S = []
            # A = int(amplitude_ent.get())
            # T = int(period_ent.get())
            # N = int(count_ent.get())
            A = int(svA.get())
            T = int(svT.get())
            N = int(svN.get())
            if str(var.get()) == "1":
                selection = "S(t)=A/2+2*A/pi*(cos(2*pi/T*t)-1/3*cos(3*2*pi/T*t)+1/5*cos(5*2*pi/T*t)-...)"
                for t in range(100):
                    tmp = 0
                    for i in range(1, N, 2):
                        if (i - 1) / 2 % 2 == 1:
                            tmp -= 1 / i * np.cos(i * 2 * np.pi / T * t)
                        else:
                            tmp += 1 / i * np.cos(i * 2 * np.pi / T * t)
                    tmp *= 2 * A / np.pi
                    tmp += A / 2
                    S.append(tmp)
            elif str(var.get()) == "2":
                selection = "S(t)=8*A/pi**2*(cos(2*pi/T*t)+1/3**2*cos(3*2*pi/T*t)+1/5**2*cos(5*2*pi/T*t)+...)"
                for t in range(100):
                    tmp = 0
                    for i in range(1, N, 2):
                        tmp += 1 / i ** 2 * np.cos(i * 2 * np.pi / T * t)
                    tmp *= 8 * A / np.pi ** 2
                    S.append(tmp)
            elif str(var.get()) == "3":
                selection = "S(t)=2*A/pi*(sin(2*pi/T*t)-1/2*sin(2*2*pi/T*t)+1/3*sin(3*2*pi/T*t)-1/4*sin(4*2*pi/T*t)+...)"
                for t in range(100):
                    tmp = 0
                    for i in range(1, N, 1):
                        if i % 2 == 0:
                            tmp -= 1 / i * np.sin(i * 2 * np.pi / T * t)
                        else:
                            tmp += 1 / i * np.sin(i * 2 * np.pi / T * t)
                    tmp *= 2 * A / np.pi
                    S.append(tmp)
            fourie_label.config(text=selection)
            plot(S)

        var = tk.IntVar()
        R1 = tk.Radiobutton(window3, text="Прямоугольноый", variable=var, value=1, command=sel).place(x=250, y=0)
        R2 = tk.Radiobutton(window3, text="Треугольный", variable=var, value=2, command=sel).place(x=250, y=20)
        R3 = tk.Radiobutton(window3, text="Пилообразноый", variable=var, value=3, command=sel).place(x=250, y=40)

        fourie_label = tk.Label(window3)
        fourie_label.place(x=0, y=150)
        window3.mainloop()

    def fractal_pifagor():
        import math

        def exit_(event):
            """Выход при нажатии ctr+z"""
            root.destroy()

        def callback(sv):
            # print(sv.get())
            canv.delete("all")

            x = 600
            y = 650
            side = 100
            deep = int(sv.get())
            alfa = math.pi / 3

            canv.create_rectangle(0, 1200, 1800, 1200 - y, fill="#ADFF2F")

            draw_tree(x / 2 - 100, y - 100, side / 2, math.pi / 2, alfa * 3 / 4, deep, 1)
            draw_tree(x, y, side, math.pi / 2, alfa, deep, 1)

        def draw_tree(x, y, side, fi, alfa, deep, count_deep):
            """Рекурсивно рисует дерево пифагора"""
            x1 = x
            y1 = y

            dx = side * math.sin(fi)
            dy = side * math.cos(fi)

            x2 = x + dx
            y2 = y - dy

            x3 = x + dx - dy
            y3 = y - dy - dx

            x4 = x - dy
            y4 = y - dx

            x5 = x - dy + side * math.cos(alfa) * math.sin(fi - alfa)
            y5 = y - dx - side * math.cos(alfa) * math.cos(fi - alfa)

            if count_deep < 5:
                colour = "#" + str(count_deep * 20) + "0000"
            elif count_deep < 9:
                colour = "#00" + str(count_deep * 10) + "00"
            else:
                colour = "#009900"

            canv.create_polygon(x1, y1, x2, y2, x3, y3, x4, y4, fill=colour)
            canv.create_polygon(x4, y4, x3, y3, x5, y5, fill=colour)

            if deep > 1:
                draw_tree(x5, y5, side * math.sin(alfa), fi - alfa + math.pi / 2, alfa, deep - 1, count_deep + 1)
                draw_tree(x4, y4, side * math.cos(alfa), fi - alfa, alfa, deep - 1, count_deep + 1)

        # инициализация окна
        window4 = tk.Toplevel(window)
        window4.title("Регулярные фракталы дерева Пифагора")
        window4.geometry("1800x1200")

        svN = tk.StringVar(value=7)  # начальное значение 7
        svN.trace("w", lambda name, index, mode, sv=svN: callback(sv))

        count_lbl = tk.Label(window4, text="Число рекурсивных вызовов:")
        count_lbl.place(x=0, y=0)
        spinbox = tk.Spinbox(window4, from_=1.0, to=15.0, textvariable=svN)
        spinbox.place(x=200, y=0)

        # создание холста
        canv = tk.Canvas(window4, width=1800, height=1200, bg="lightblue")
        canv.place(x=0, y=20)

        x = 600
        y = 650
        side = 100
        deep = 7
        alfa = math.pi / 3

        canv.create_rectangle(0, 1200, 1800, 1200 - y, fill="#ADFF2F")

        draw_tree(x / 2 - 100, y - 100, side / 2, math.pi / 2, alfa * 3 / 4, deep, 1)
        draw_tree(x, y, side, math.pi / 2, alfa, deep, 1)

        window4.mainloop()

    def fractal_serpinsii():
        import turtle

        def drawTriangle(points, color, myTurtle):
            myTurtle.fillcolor(color)
            myTurtle.up()
            myTurtle.goto(points[0][0], points[0][1])
            myTurtle.down()
            myTurtle.begin_fill()
            myTurtle.goto(points[1][0], points[1][1])
            myTurtle.goto(points[2][0], points[2][1])
            myTurtle.goto(points[0][0], points[0][1])
            myTurtle.end_fill()

        def getMid(p1, p2):
            return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

        def sierpinski(points, degree, myTurtle):
            colormap = ['blue', 'red', 'green', 'white', 'yellow',
                        'violet', 'orange']
            drawTriangle(points, colormap[degree], myTurtle)
            if degree > 0:
                sierpinski([points[0],
                            getMid(points[0], points[1]),
                            getMid(points[0], points[2])],
                           degree - 1, myTurtle)
                sierpinski([points[1],
                            getMid(points[0], points[1]),
                            getMid(points[1], points[2])],
                           degree - 1, myTurtle)
                sierpinski([points[2],
                            getMid(points[2], points[1]),
                            getMid(points[0], points[2])],
                           degree - 1, myTurtle)

        def main():
            myTurtle = turtle.Turtle()
            myWin = turtle.Screen()
            myPoints = [[-100, -50], [0, 100], [100, -50]]
            sierpinski(myPoints, 4, myTurtle)
            myWin.exitonclick()

        main()

    def recursion():
        def new_term(a1, d, n):
            if n == 1:
                res = a1
            else:
                res = new_term(a1, d, n - 1) + d
            return res

        def sum_ar(a1, d, n):
            if n == 1:
                res = a1
            else:
                res = sum_ar(a1, d, n - 1) + new_term(a1, d, n)
            return res

        window5 = tk.Toplevel(window)
        window5.title("Рекурсивный алгоритм")
        window5.geometry("550x100+880+30")

        def callback(sv):
            res_lbl.config(
                text=f"Сумма арифметической прогрессии = {sum_ar(int(A_ent.get()), int(D_ent.get()), int(N_ent.get()))}")

        svA = tk.StringVar()
        svD = tk.StringVar()
        svN = tk.StringVar()
        svA.trace("w", lambda name, index, mode, sv=svA: callback(sv))
        svD.trace("w", lambda name, index, mode, sv=svD: callback(sv))
        svN.trace("w", lambda name, index, mode, sv=svN: callback(sv))

        A_lbl = tk.Label(window5, text="Первый член арифметической прогрессии (а1):")
        A_lbl.place(x=0, y=0)
        A_ent = tk.Entry(window5, width=10, textvariable=svA)
        A_ent.place(x=310, y=0)

        D_lbl = tk.Label(window5, text="Приращение арифметической прогрессии (d):")
        D_lbl.place(x=0, y=25)
        D_ent = tk.Entry(window5, width=10, textvariable=svD)
        D_ent.place(x=310, y=25)

        N_lbl = tk.Label(window5, text="Длина арифметической прогрессии (N):")
        N_lbl.place(x=0, y=50)
        N_ent = tk.Entry(window5, width=10, textvariable=svN)
        N_ent.place(x=310, y=50)

        res_lbl = tk.Label(window5, text="Сумма арифметической прогрессии =")
        res_lbl.place(x=0, y=75)

        window5.mainloop()

    def dop3():
        import words as wd
        from tkinter import messagebox

        def get_word():
            import random
            return random.choice(wd.wordslist)

        window6 = tk.Toplevel(window)
        window6.title("Доп — Wordle")
        # window6.geometry("550x100+880+30")
        word = get_word()

        GREEN = "#69AA65"
        YELLOW = "#C9B359"
        BLACK = "#000000"
        GRAY = "#777C7F"
        WHITE = "#FFFFFF"

        # root.config(bg=BLACK)

        # guessnum = 1

        guessnum_lbl = tk.Label(window6, text="Попытка 1:")
        guessnum_lbl.grid(row=999, column=0, padx=10, pady=10, columnspan=1)

        wordInput = tk.Entry(window6)
        wordInput.grid(row=999, column=1, padx=10, pady=10, columnspan=3)

        def getGuess():
            guess = wordInput.get()
            guessnum = int(guessnum_lbl.cget("text")[-2])
            print(word)

            if guessnum <= 6:
                if len(guess) == 5:
                    if word == guess:  # CORRECT
                        messagebox.showinfo("Угадано!", f"Ура, вы угадали слово: {word.title()}")
                    else:  # INCORRECT
                        guessnum += 1
                        for i, letter in enumerate(guess):
                            label = tk.Label(window6, text=letter.upper())
                            label.grid(row=guessnum, column=i, padx=10, pady=10)

                            if letter == word[i]:  # if they get the letter right
                                label.config(bg=GREEN, fg=WHITE)
                            if letter in word and not letter == word[i]:  # if the letter is in the word, but not in the right spot
                                label.config(bg=YELLOW, fg=WHITE)
                            if letter not in word:
                                label.config(bg=GRAY, fg=WHITE)
                else:
                    messagebox.showerror("Слово должно состоять из 5 букв",
                                         "Пожалуйста, напишите слово, состоящее из 5 букв")
            else:
                messagebox.showerror("Вы проиграли!", f"К сожалению, вам не удалось угадать слово! Это было: {word}")
            guessnum_lbl.config(text=f"Попытка {guessnum}:")

        wordGuessButton = tk.Button(window6, text="Угадать", command=getGuess)
        wordGuessButton.grid(row=999, column=4, columnspan=1)

        window6.mainloop()

    def more3():
        window2 = tk.Toplevel(window)
        window2.title("Что показать еще")
        window2.geometry("+475+175")

        window2.columnconfigure(3, weight=1)
        window2.rowconfigure(2, weight=1)

        fourie_btn = tk.Button(window2, text="«Живые» сигналы Фурье", width=24, command=fourie)
        fourie_btn.grid(row=0, column=0, columnspan=2)

        recursion_btn = tk.Button(window2, text="Рекурсия", width=10, command=recursion)
        recursion_btn.grid(row=0, column=2)

        fractal_pifagor_btn = tk.Button(window2, text="Пифагор", width=10, command=fractal_pifagor)
        fractal_pifagor_btn.grid(row=1, column=0)

        fractal_serpinsii_btn = tk.Button(window2, text="Серпинский", width=10, command=fractal_serpinsii)
        fractal_serpinsii_btn.grid(row=1, column=1)

        dop_btn = tk.Button(window2, text="Доп", width=10, command=dop3)
        dop_btn.grid(row=1, column=2)

        app.mainloop()

    class Paint(tk.Frame):

        def __init__(self, parent):
            tk.Frame.__init__(self, parent)

            self.parent = parent
            self.color = "black"
            self.brush_size = 2
            self.setUI()

        def open_img(self):
            x = filedialog.askopenfilename()  # Select the Imagename  from a folder

            # opens the image
            self.img = Image.open(x)
            self.tatras = ImageTk.PhotoImage(self.img)
            self.canv.create_image(0, 0, anchor=tk.NW, image=self.tatras)

        def save_widget_as_image(self, widget):
            x = filedialog.asksaveasfilename()
            ImageGrab.grab(bbox=(
                widget.winfo_rootx(),
                widget.winfo_rooty(),
                widget.winfo_rootx() + widget.winfo_width(),
                widget.winfo_rooty() + widget.winfo_height()
            )).save(x)

        def set_color(self, new_color):
            self.color = new_color

        def set_brush_size(self, new_size):
            self.brush_size = new_size

        def draw(self, event):
            self.canv.create_oval(event.x - self.brush_size,
                                  event.y - self.brush_size,
                                  event.x + self.brush_size,
                                  event.y + self.brush_size,
                                  fill=self.color, outline=self.color)

        def setUI(self):
            self.parent.title("Виндоус Форма")  # Устанавливаем название окна
            self.pack(fill=tk.BOTH, expand=1)  # Размещаем активные элементы на родительском окне

            self.columnconfigure(6,
                                 weight=1)  # Даем седьмому столбцу возможность растягиваться, благодаря чему кнопки не будут разъезжаться при ресайзе
            self.rowconfigure(2, weight=1)  # То же самое для третьего ряда

            self.canv = tk.Canvas(self, bg="white")  # Создаем поле для рисования, устанавливаем белый фон
            self.canv.grid(row=2, column=0, columnspan=7,
                           padx=5, pady=5,
                           sticky=tk.E + tk.W + tk.S + tk.N)  # Прикрепляем канвас методом grid. Он будет находится в 3м ряду, первой колонке, и будет занимать 7 колонок, задаем отступы по X и Y в 5 пикселей, и заставляем растягиваться при растягивании всего окна
            self.canv.bind("<B1-Motion>",
                           self.draw)  # Привязываем обработчик к канвасу. <B1-Motion> означает "при движении зажатой левой кнопки мыши" вызывать функцию draw

            color_lab = tk.Label(self, text="Цвет: ")  # Создаем метку для кнопок изменения цвета кисти
            color_lab.grid(row=0, column=0,
                           padx=6)  # Устанавливаем созданную метку в первый ряд и первую колонку, задаем горизонтальный отступ в 6 пикселей

            red_btn = tk.Button(self, text="Красный", width=10,
                                command=lambda: self.set_color(
                                    "red"))  # Создание кнопки:  Установка текста кнопки, задание ширины кнопки (10 символов), функция вызываемая при нажатии кнопки.
            red_btn.grid(row=0, column=1)  # Устанавливаем кнопку

            # Создание остальных кнопок повторяет ту же логику, что и создание кнопки установки красного цвета, отличаются лишь аргументы.

            green_btn = tk.Button(self, text="Зеленый", width=10,
                                  command=lambda: self.set_color("green"))
            green_btn.grid(row=0, column=2)

            blue_btn = tk.Button(self, text="Синий", width=10,
                                 command=lambda: self.set_color("blue"))
            blue_btn.grid(row=0, column=3)

            black_btn = tk.Button(self, text="Черный", width=10,
                                  command=lambda: self.set_color("black"))
            black_btn.grid(row=0, column=4)

            white_btn = tk.Button(self, text="Белый", width=10,
                                  command=lambda: self.set_color("white"))
            white_btn.grid(row=0, column=5)

            clear_btn = tk.Button(self, text="Очистить все", width=10,
                                  command=lambda: self.canv.delete("all"))
            clear_btn.grid(row=1, column=4, sticky=tk.W)

            size_lab = tk.Label(self, text="Размер кисти: ")
            size_lab.grid(row=1, column=0, padx=5)
            one_btn = tk.Button(self, text="Маленький", width=10,
                                command=lambda: self.set_brush_size(5))
            one_btn.grid(row=1, column=1)

            more_btn = tk.Button(self, text="Еще", width=10, command=more3)
            more_btn.grid(row=0, column=6, sticky=tk.W)

            # two_btn = tk.Button(self, text="Five", width=10,
            #                     command=lambda: self.set_brush_size(5))
            # two_btn.grid(row=1, column=2)

            # five_btn = tk.Button(self, text="Seven", width=10,
            #                      command=lambda: self.set_brush_size(7))
            # five_btn.grid(row=1, column=3)

            seven_btn = tk.Button(self, text="Средний", width=10,
                                  command=lambda: self.set_brush_size(20))
            seven_btn.grid(row=1, column=2)

            # ten_btn = tk.Button(self, text="Twenty", width=10,
            #                     command=lambda: self.set_brush_size(20))
            # ten_btn.grid(row=1, column=3)

            twenty_btn = tk.Button(self, text="Большой", width=10,
                                   command=lambda: self.set_brush_size(35))
            twenty_btn.grid(row=1, column=3, sticky=tk.W)

            two_btn = tk.Button(self, text="Открыть", width=10,
                                command=lambda: self.open_img())
            two_btn.grid(row=1, column=5)

            five_btn = tk.Button(self, text="Сохранить", width=10,
                                 command=lambda: self.save_widget_as_image(self.canv))
            five_btn.grid(row=1, column=6, sticky=tk.W)
            # self.mainloop()

    if __name__ == '__main__':
        app = Paint(window)
        app.mainloop()


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
filemenu.add_command(label="ЛР 3", command=lab3_btn)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.destroy)
menubar.add_cascade(label="Технологии и методы программирования", menu=filemenu)

helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="About...", command=about_btn)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

root.mainloop()
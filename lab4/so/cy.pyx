import tkinter as tk
import random

def prh():
    print("hello")

root = tk.Tk()
root.geometry("850x200")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

lbl_exceptions = tk.Label(root, background="white", anchor="nw", justify="left")
lbl_exceptions.grid(row=0, column=0, columnspan=5, padx=5, pady=5, sticky=tk.E + tk.W + tk.S + tk.N)


def main_parser(signature):
    file = open("/Users/vadim/PycharmProjects/pythonProject7/exceptions.txt", "r")
    data = file.read()
    return data.count(signature)
    # file.close()

occurrences2 = main_parser("pythonProject4")
occurrences3 = main_parser("pythonProject5")
occurrences4 = main_parser("pythonProject7")

lbl_exceptions_in1 = tk.Label(root, text=f"Project1: {random.randint(200, 400)}")
lbl_exceptions_in1.grid(row=1, column=0)
lbl_exceptions_in2 = tk.Label(root, text=f"Project2: {occurrences2}")
lbl_exceptions_in2.grid(row=1, column=1, padx=100)
lbl_exceptions_in3 = tk.Label(root, text=f"Project3: {occurrences3}")
lbl_exceptions_in3.grid(row=1, column=2, padx=140)
lbl_exceptions_in4 = tk.Label(root, text=f"Project4: {occurrences4}")
lbl_exceptions_in4.grid(row=1, column=3)

# ——————————————————————————————————————

def lab4_btn():
    from tkinter import ttk
    window_last = tk.Toplevel(root)
    window_last.geometry("850x500+5+300")
    window_last.title("Виндоус Форма")

    def correct_inputH(text):
        if text.isdigit() and int(text) in range(24):
            valid = True
        else:
            valid = False
        return valid

    def correct_inputMS(text):
        if text.isdigit() and int(text) in range(60):
            valid = True
        else:
            valid = False
        return valid

    vcmdH = (window_last.register(correct_inputH), '%P')
    vcmdMS = (window_last.register(correct_inputMS), '%P')

    hourstr1 = tk.StringVar(window_last, '20')
    hour1 = tk.Spinbox(window_last, from_=0, to=23, wrap=True,
                       textvariable=hourstr1, width=3,
                       validate='all', validatecommand=vcmdH)
    minstr1 = tk.StringVar(window_last, '00')
    min1 = tk.Spinbox(window_last, from_=0, to=59, wrap=True,
                      textvariable=minstr1, width=3,
                      validate='all', validatecommand=vcmdMS)
    secstr1 = tk.StringVar(window_last, '00')
    sec1 = tk.Spinbox(window_last, from_=0, to=59, wrap=True,
                      textvariable=secstr1, width=3,
                      validate='all', validatecommand=vcmdMS)

    hourstr2 = tk.StringVar(window_last, '23')
    hour2 = tk.Spinbox(window_last, from_=0, to=23, wrap=True,
                       textvariable=hourstr2, width=3,
                       validate='all', validatecommand=vcmdH)
    minstr2 = tk.StringVar(window_last, '59')
    min2 = tk.Spinbox(window_last, from_=0, to=59, wrap=True,
                      textvariable=minstr2, width=3,
                      validate='all', validatecommand=vcmdMS)
    secstr2 = tk.StringVar(window_last, '59')
    sec2 = tk.Spinbox(window_last, from_=0, to=59, wrap=True,
                      textvariable=secstr2, width=3,
                      validate='all', validatecommand=vcmdMS)

    time_from_lbl = tk.Label(window_last, text="от")
    time_from_lbl.grid(row=1, column=1, sticky=tk.W)
    hour1.grid(row=1, column=1, sticky=tk.W, padx=20)
    min1.grid(row=1, column=1, sticky=tk.W, padx=75)
    sec1.grid(row=1, column=1, sticky=tk.W, padx=130)

    time_to_lbl = tk.Label(window_last, text="до")
    time_to_lbl.grid(row=1, column=1, sticky=tk.E, padx=200)
    hour2.grid(row=1, column=1, sticky=tk.E, padx=150)
    min2.grid(row=1, column=1, sticky=tk.E, padx=95)
    sec2.grid(row=1, column=1, sticky=tk.E, padx=40)

    # App(window_last).grid(row=1, column=1)
    def time_compare(time_to_check):
        time_to_check = time_to_check.split(":")
        time_to_check = (int(time_to_check[0])*60+int(time_to_check[1]))*60+int(time_to_check[2])
        time_from, time_to = get_input_time()
        if time_to < time_from:
            time_to += 24*60*60
            if time_to_check < time_from:
                time_to_check += 24*60*60 #20 00 00 - 00 30 00 ___ 00 20 00
        if time_from <= time_to_check <= time_to:
            return True
        else:
            return False

    def string_modify():
        email = "kidavspb2002@gmail.com"

        start = textWidget.index(1.0)
        end = textWidget.index("end")
        textWidget.mark_set("matchStart", start)
        textWidget.mark_set("matchEnd", start)
        textWidget.mark_set("searchLimit", end)

        count = tk.IntVar()
        num_all = 0
        num_found = 0
        while True:
            index = textWidget.search("string", "matchEnd", "searchLimit", count=count, regexp=False)
            if index == "": break
            if count.get() == 0: break  # degenerate pattern which matches zero-length strings

            search_idx = search_idx_0 = found = -1
            while search_idx_0 < int(index.split(".")[0]):
                found = search_idx_0
                search_idx = textWidget.search("Traceback", "matchEnd", "searchLimit", regexp=False)
                if search_idx == "": break
                search_idx_0 = int(search_idx.split(".")[0])
                textWidget.mark_set("matchStart", search_idx)
                textWidget.mark_set("matchEnd", "%s+%sc" % (search_idx, 9))
            if found == -1: break
            search_idx = f"{found-1}.12"
            search_idx_to = f"{found-1}.21"
            time_to_check = textWidget.get(search_idx, search_idx_to)
            if time_compare(time_to_check):
                # temp = str(index.split(".")[0])+str(int(index.split(".")[1])+count.get())
                textWidget.insert("%s+%sc" % (index, count.get()), email)
                num_found+=1

            textWidget.mark_set("matchStart", index)
            textWidget.mark_set("matchEnd", "%s+%sc" % (index, count.get()))
            hexadecimal = str(''.join([random.choice('ABCDEF0123456789') for i in range(6)]))
            textWidget.tag_configure(hexadecimal, foreground="hotpink")
            textWidget.tag_add(hexadecimal, "matchStart", "matchEnd")

            textWidget.mark_set("matchStart", "%s+%sc" % (index, count.get()))
            textWidget.mark_set("matchEnd", "%s+%sc" % (index, count.get()+len(email)))
            hexadecimal = str(''.join([random.choice('ABCDEF0123456789') for i in range(6)]))
            textWidget.tag_configure(hexadecimal, foreground="greenyellow")
            textWidget.tag_add(hexadecimal, "matchStart", "matchEnd")
            num_all+=1
        sig_num_lbl.config(text=f"встречено {num_all} раз (в выбранное время попало {num_found} раз)")

    def highlight_pattern(pattern, tag, start="1.0", end="end", regexp=False):
        '''Apply the given tag to all text that matches the given pattern

        If 'regexp' is set to True, pattern will be treated as a regular
        expression according to Tcl's regular expression syntax.
        '''

        start = textWidget.index(start)
        end = textWidget.index(end)
        textWidget.mark_set("matchStart", start)
        textWidget.mark_set("matchEnd", start)
        textWidget.mark_set("searchLimit", end)

        count = tk.IntVar()
        num = 0
        while True:
            index = textWidget.search(pattern, "matchEnd", "searchLimit", count=count, regexp=regexp)
            if index == "": break
            if count.get() == 0: break  # degenerate pattern which matches zero-length strings
            textWidget.mark_set("matchStart", index)
            textWidget.mark_set("matchEnd", "%s+%sc" % (index, count.get()))
            textWidget.tag_add(tag, "matchStart", "matchEnd")
            num+=1
        return num

    def get_input_time():
        from_t = (int(hourstr1.get()) * 60 + int(minstr1.get())) * 60 + int(secstr1.get())
        to_t = (int(hourstr2.get()) * 60 + int(minstr2.get())) * 60 + int(secstr2.get())
        return from_t, to_t

    def find_sig():
        # import re
        import random

        selection = combobox.get()  # получаем выделенный элемент
        print(f"Вы выбрали: {selection}")

        if selection.lower() == "string":
            string_modify()
        else:
            colors = ["aquamarine4", "blue", "blueviolet", "brown1", "burntumber", "cadmiumorange", "chartreuse4",
                      "yellow1"]
            hexadecimal = str(''.join([random.choice('ABCDEF0123456789') for i in range(6)]))
            rand_color = colors[random.randint(0, len(colors) - 1)]

            # print(f"и {get_input_time()[0]} - {get_input_time()[1]}")

            textWidget.tag_configure(hexadecimal, foreground=rand_color)  # configuring a tag with a certain style (font color)
            num = highlight_pattern(selection, hexadecimal)  # apply the tag "red"
            sig_num_lbl.config(text=f"встречено {num} раз")

    sig_lbl = tk.Label(window_last, text="Сигнатура")
    sig_lbl.grid(row=0, column=0)
    sig_num_lbl = tk.Label(window_last)
    sig_num_lbl.grid(row=0, column=1, sticky=tk.W)

    signatures = ["вирус", "pythonProject4", "pythonProject5", "pythonProject7", "string"]

    combobox = ttk.Combobox(window_last, values=signatures, width=10)
    combobox.grid(row=1, column=0)
    # combobox.bind("<<ComboboxSelected>>", selected)

    find_btn = tk.Button(window_last, text="Найти включения", width=10, command=lambda: find_sig())
    find_btn.grid(row=2, column=1)
    textWidget = tk.Text(window_last)
    textWidget.grid(row=3, column=0, columnspan=10)

    root.mainloop()


def donothing():
    filewin = tk.Toplevel(root)
    lbl_nothing = tk.Label(filewin, text="There is nothing to see here", padx=100, pady=100)
    lbl_nothing.pack()


menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="ЛР 1", command=donothing)
filemenu.add_command(label="ЛР 4", command=lab4_btn)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.destroy)
menubar.add_cascade(label="Технологии и методы программирования", menu=filemenu)

helpmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

root.mainloop()
